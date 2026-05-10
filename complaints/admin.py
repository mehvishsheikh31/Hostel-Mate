from django.contrib import admin
from .models import Complaint, StudentProfile


# ✅ NEW: StudentProfile visible and manageable in admin panel
@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'hostel_block', 'room_no']
    search_fields = ['user__username', 'hostel_block', 'room_no']
    ordering = ['user__username']


# ✅ IMPROVED: Complaint admin with filters, search, and bulk actions
@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):

    # Columns shown in the complaints list
    list_display = [
        'id', 'title', 'user', 'category',
        'priority', 'status', 'hostel_block',
        'room_no', 'created_at', 'resolved_at'
    ]

    # ✅ Filter sidebar on the right
    list_filter = ['status', 'category', 'priority', 'hostel_block']

    # ✅ Search by title, student name, or room number
    search_fields = ['title', 'user__username', 'room_no']

    # ✅ Click status directly in the list to change it (no need to open each complaint)
    list_editable = ['status']

    # ✅ Default ordering — newest complaints first
    ordering = ['-created_at']

    # ✅ Read-only fields that should never be manually edited
    readonly_fields = ['created_at', 'updated_at', 'resolved_at']

    # ✅ Organized sections inside the complaint detail page
    fieldsets = (
        ('Complaint Info', {
            'fields': ('user', 'title', 'description', 'category', 'priority', 'image')
        }),
        ('Location', {
            'fields': ('hostel_block', 'room_no')
        }),
        ('Status & Remarks', {
            'fields': ('status', 'admin_remarks')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'resolved_at'),
            'classes': ('collapse',)   # hidden by default, click to expand
        }),
    )

    # ✅ Bulk action: mark selected complaints as resolved at once
    actions = ['mark_resolved', 'mark_in_progress']

    def mark_resolved(self, request, queryset):
        for complaint in queryset:
            complaint.status = 'Resolved'
            complaint.save()   # triggers our custom save() in models.py
        self.message_user(request, f"{queryset.count()} complaint(s) marked as Resolved.")
    mark_resolved.short_description = "Mark selected as Resolved"

    def mark_in_progress(self, request, queryset):
        queryset.update(status='In Progress')
        self.message_user(request, f"{queryset.count()} complaint(s) marked as In Progress.")
    mark_in_progress.short_description = "Mark selected as In Progress"