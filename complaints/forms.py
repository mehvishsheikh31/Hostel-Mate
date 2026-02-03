from django import forms
from .models import Complaint

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['title', 'description', 'category', 'priority', 'hostel_block', 'room_no', 'image']

class StatusUpdateForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['status', 'admin_remarks']