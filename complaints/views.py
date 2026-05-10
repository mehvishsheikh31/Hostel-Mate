from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Count
from django.contrib import messages
from django.http import HttpResponse
import json
import csv

from .models import Complaint
from .forms import ComplaintForm, StatusUpdateForm


# ✅ FIX 1: Moved is_admin to top so decorators can use it cleanly
def is_admin(user):
    return user.is_staff


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! Welcome aboard.')
            return redirect('student_dashboard')
        else:
            messages.error(request, 'Registration failed. Please correct the errors.')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def student_dashboard(request):
    if request.user.is_staff:
        return redirect('admin_dashboard')

    if request.method == 'POST':
        form = ComplaintForm(request.POST, request.FILES)
        if form.is_valid():
            complaint_obj = form.save(commit=False)
            complaint_obj.user = request.user
            complaint_obj.save()
            messages.success(request, 'Complaint submitted successfully!')
            return redirect('student_dashboard')
        else:
            messages.error(request, 'Please correct the errors in the form.')
    else:
        form = ComplaintForm()

    my_complaints = Complaint.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'student_dashboard.html', {'form': form, 'complaints': my_complaints})


@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('student_dashboard')

    complaints = Complaint.objects.all().order_by('-created_at')

    status_filter = request.GET.get('status')
    if status_filter:
        complaints = complaints.filter(status=status_filter)

    total = Complaint.objects.count()
    pending = Complaint.objects.filter(status='Pending').count()
    resolved = Complaint.objects.filter(status='Resolved').count()
    in_progress = Complaint.objects.filter(status='In Progress').count()

    # ✅ FIX 2: Was 6 DB queries in a loop — now just 1 query
    categories = ['Water', 'Electricity', 'Cleaning', 'Internet', 'Furniture', 'Other']
    cat_counts = (
        Complaint.objects
        .values('category')
        .annotate(count=Count('id'))
    )
    cat_count_map = {item['category']: item['count'] for item in cat_counts}
    bar_data = json.dumps([cat_count_map.get(cat, 0) for cat in categories])

    pie_data = json.dumps([pending, in_progress, resolved])

    context = {
        'complaints': complaints,
        'total': total,
        'pending': pending,
        'resolved': resolved,
        'in_progress': in_progress,
        'pie_data': pie_data,
        'bar_data': bar_data,
        'bar_labels': json.dumps(categories),
    }

    return render(request, 'admin_dashboard.html', context)


@login_required
def update_complaint(request, pk):
    if not request.user.is_staff:
        return redirect('student_dashboard')

    complaint_obj = get_object_or_404(Complaint, pk=pk)

    if request.method == 'POST':
        form = StatusUpdateForm(request.POST, instance=complaint_obj)
        if form.is_valid():
            form.save()
            messages.success(request, f'Complaint #{pk} updated successfully!')
            return redirect('admin_dashboard')
    else:
        form = StatusUpdateForm(instance=complaint_obj)

    return render(request, 'update_complaint.html', {'form': form, 'complaint': complaint_obj})


@login_required
def export_complaints(request):
    if not request.user.is_staff:
        return redirect('student_dashboard')

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="hostel_complaints.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Title', 'Student', 'Room', 'Category', 'Priority', 'Status', 'Date'])

    complaints_list = Complaint.objects.all().values_list(
        'id', 'title', 'user__username', 'room_no',
        'category', 'priority', 'status', 'created_at'
    )
    for c in complaints_list:
        writer.writerow(c)

    return response


# ✅ FIX 3: Added login_url='login' so it redirects to YOUR login page, not Django's default /accounts/login/
@login_required
@user_passes_test(is_admin, login_url='login')
def delete_complaint(request, id):
    complaint = get_object_or_404(Complaint, id=id)
    if request.method == 'POST':
        complaint.delete()
        messages.success(request, 'Complaint deleted successfully.')
    return redirect('admin_dashboard')