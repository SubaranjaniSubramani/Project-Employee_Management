from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('home/',views.Home,name='Home'),
    path('admin/',views.Admin_login,name='Admin_login'),
    path('admin_dashboard/',views.Admin_dashboard,name='Admin_dashboard'),
    path('add_emp/',views.Add_employee,name="Add_employee"),
    path('emp_list/',views.Employee_list,name="Employee_list"),
    path('update/<int:id>/',views.Update_employee,name="Update_employee"),
    path('delete/<int:id>/',views.Delete_employee,name="Delete_employee"),
     path(
        'employee_login/',
        views.Employee_login,
        name='Employee_login'
    ),

    path(
        'employee_profile/<int:id>/',
        views.Employee_profile,
        name='Employee_profile'
    ),

    # Attendance
    path(
        'add_attendance/',
        views.Add_attendance,
        name='Add_attendance'
    ),

    path(
        'attendance_list/',
        views.Attendance_list,
        name='Attendance_list'
    ),

    # Leave Request
    path(
        'leave_request/',
        views.Leave_request,
        name='Leave_request'
    ),

    path(
        'leave_list/',
        views.Leave_list,
        name='Leave_list'
    ),

    # Salary
    path(
        'add_salary/',
        views.Add_salary,
        name='Add_salary'
    ),

    path(
        'salary_list/',
        views.Salary_list,
        name='Salary_list'
    ),
    path(
    'approve_leave/<int:id>/',
    views.Approve_leave,
    name='Approve_leave'
),

path(
    'reject_leave/<int:id>/',
    views.Reject_leave,
    name='Reject_leave'
),

path(
    'logout/',
    views.Logout,
    name='Logout'
),


]