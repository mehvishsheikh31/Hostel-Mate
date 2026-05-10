from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# ✅ NEW: StudentProfile stores room/block once per student
# so they don't have to retype it on every complaint
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    hostel_block = models.CharField(max_length=50)
    room_no = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user.username} — Block {self.hostel_block}, Room {self.room_no}"


class Complaint(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]
    CATEGORY_CHOICES = [
        ('Water', 'Water'),
        ('Electricity', 'Electricity'),
        ('Cleaning', 'Cleaning'),
        ('Internet', 'Internet'),
        ('Furniture', 'Furniture'),
        ('Other', 'Other'),
    ]
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    hostel_block = models.CharField(max_length=50)
    room_no = models.CharField(max_length=10)
    image = models.ImageField(upload_to='complaints/', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    admin_remarks = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # ✅ NEW: Track exactly when a complaint was resolved
    resolved_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # ✅ Auto-set resolved_at when status changes to Resolved
        if self.status == 'Resolved' and self.resolved_at is None:
            self.resolved_at = timezone.now()
        # ✅ Clear resolved_at if admin reopens the complaint
        elif self.status != 'Resolved':
            self.resolved_at = None
        super().save(*args, **kwargs)

    # ✅ Helper: how many days did it take to resolve?
    @property
    def resolution_time_days(self):
        if self.resolved_at and self.created_at:
            delta = self.resolved_at - self.created_at
            return delta.days
        return None

    def __str__(self):
        return f"{self.title} — {self.user.username} ({self.status})"