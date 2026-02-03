from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('dashboard/', views.student_dashboard, name='student_dashboard'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('update/<int:pk>/', views.update_complaint, name='update_complaint'),
    path('export/', views.export_complaints, name='export_complaints'),
    path('delete_complaint/<int:id>/', views.delete_complaint, name='delete_complaint'),
]