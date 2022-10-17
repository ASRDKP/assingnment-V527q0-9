from rest_framework import serializers
from EmployeeApp.models import Department, Employees


class DepartmentSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('DepartmentID','DepartmentName')
        # fields = '__all__'
    

class EmployeesSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('EmployeesID','EmployeesName','Department', 'DateOfJoining', 'PhotoFileName')
        
