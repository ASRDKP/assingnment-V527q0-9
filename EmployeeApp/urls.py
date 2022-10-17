from django.urls import path
from django.urls import re_path
from EmployeeApp import views

urlpatterns = [
    path(r'department',views.departmentApi),
    re_path(r'department/(?P<id>\d+)',views.departmentApi),
    
    path(r'employee',views.employeeApi),
    re_path(r'employee/(?P<id>\d+)',views.employeeApi),
]

trailingslash=False