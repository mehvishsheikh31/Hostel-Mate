from django import forms
from .models import Complaint


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['title', 'description', 'category', 'priority', 'hostel_block', 'room_no', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Water leakage in bathroom'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe the problem in detail...',
                'rows': 4
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            }),
            'priority': forms.Select(attrs={
                'class': 'form-select'
            }),
            'hostel_block': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. A'
            }),
            'room_no': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. 101'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }

    # ✅ FIX 1: Validate file type — only allow JPG, JPEG, PNG
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            allowed_extensions = ['.jpg', '.jpeg', '.png']
            ext = '.' + image.name.split('.')[-1].lower()
            if ext not in allowed_extensions:
                raise forms.ValidationError("Only JPG and PNG images are allowed.")

            # ✅ FIX 2: Limit file size to 2MB
            max_size_mb = 2
            if image.size > max_size_mb * 1024 * 1024:
                raise forms.ValidationError(f"Image size must be under {max_size_mb}MB.")

        return image


class StatusUpdateForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['status', 'admin_remarks']
        widgets = {
            'status': forms.Select(attrs={
                'class': 'form-select'
            }),
            'admin_remarks': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Add remarks for the student...',
                'rows': 3
            }),
        }