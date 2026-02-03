from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Complaint
from .forms import ComplaintForm, StatusUpdateForm
from django.db.models import Count
from django.contrib import messages
import json
import csv
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test # <--- IMPORTANT
from .models import Complaint

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
    
    # Handle new complaint submission
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


# Make sure you have these imports at the top
import json
from django.db.models import Count

# Helper function to check if user is admin
def is_admin(user):
    return user.is_superuser
@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('student_dashboard')
    
    # 1. Get all complaints
    complaints = Complaint.objects.all().order_by('-created_at')
    
    # 2. Filter logic (Optional: keep if you want filters)
    status_filter = request.GET.get('status')
    if status_filter:
        complaints = complaints.filter(status=status_filter)

    # 3. Calculate Numbers for Top Cards
    total = Complaint.objects.count()
    pending = Complaint.objects.filter(status='Pending').count()
    resolved = Complaint.objects.filter(status='Resolved').count()
    in_progress = Complaint.objects.filter(status='In Progress').count()

    # 4. Prepare Data for Charts (JSON format)
    # Pie Chart Data (Status)
    pie_data = json.dumps([pending, in_progress, resolved])
    
    # Bar Chart Data (Categories)
    categories = ['Water', 'Electricity', 'Cleaning', 'Internet', 'Furniture', 'Other']
    bar_data_list = []
    for cat in categories:
        count = Complaint.objects.filter(category=cat).count()
        bar_data_list.append(count)
    bar_data = json.dumps(bar_data_list)

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

    complaints_list = Complaint.objects.all().values_list('id', 'title', 'user__username', 'room_no', 'category', 'priority', 'status', 'created_at')
    
    for c in complaints_list:
        writer.writerow(c)

    return response

# Add this import at the top if not present:

@user_passes_test(is_admin)
def delete_complaint(request, id):
    complaint = get_object_or_404(Complaint, id=id)
    complaint.delete()
    return redirect('admin_dashboard')