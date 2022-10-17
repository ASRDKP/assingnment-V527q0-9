from logging import exception
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser 
from django.http.response import JsonResponse
from EmployeeApp.models import Employees, Department
from EmployeeApp.serializers import DepartmentSerailizer, EmployeesSerailizer



# Create your views here.

@csrf_exempt
def departmentApi(request,id="0"):
    if request.method == "GET":
        print("Enter in  the department")
        try:         
            department = Department.objects.all()
            # print("Message from department: " , department)
            department_serailizer = DepartmentSerailizer(department,many=True)
            # print("Message from department: " , department_serailizer)
            return JsonResponse(department_serailizer.data,safe=False)
        except Exception as e:
            print("Error message in GET : " , e )
    
    elif request.method == "POST":
        try:
            department_data = JSONParser().parse(request)
            department_serailizer = DepartmentSerailizer(data=department_data)
            if department_serailizer.is_valid():
                department_serailizer.save()
                return JsonResponse("Added Successfully",safe=False)
            return JsonResponse("Fails to Add",safe=False)
        except Exception as e:
            print("Error message in POST : " , e )
   
    elif request.method == "PUT":
        try:
            department_data = JSONParser().parse(request)
            department = Department.objects.get(DepartmentID=department_data["DepartmentID"])
            department_serailizer = DepartmentSerailizer(department,data=department_data)
            if department_serailizer.is_valid():
                department_serailizer.save()
                return JsonResponse("Update Successfully",safe=False)
            return JsonResponse("Fails to Update",safe=False)
        except Exception as e:
            print("Error message in PUT : " , e )
   
    elif request.method == "DELETE":
        try:
            print('Entery in Delete Method')
            department = Department.objects.get(DepartmentID=id)
            department.delete()
            return JsonResponse("Delete Successfully",safe=False)
        except Exception as e:
            print("Error message in Delete : " , e )        
            
            
            
            


@csrf_exempt
def employeeApi(request,id="0"):
    if request.method == "GET":
        print("Enter in  the employee")
        try:         
            employee = Employees.objects.all()
            employee_serailizer = EmployeesSerailizer(employee,many=True)
            try:
                print(" Message in Post : ",employee_serailizer.data)    
            except Exception as e:
                print(" Message in Post error: ",e)
            return JsonResponse(employee_serailizer.data,safe=False)
        except Exception as e:
            print("Error message in GET : " , e )
    
    elif request.method == "POST":
        try:
            employee_data = JSONParser().parse(request)
            employee_serailizer = EmployeesSerailizer(data=employee_data)
            if employee_serailizer.is_valid():
                employee_serailizer.save()
                return JsonResponse("Added Successfully",safe=False)
            return JsonResponse("Fails to Add",safe=False)
        except Exception as e:
            print("Error message in POST : " , e )
   
    elif request.method == "PUT":
        try:
            employee_data = JSONParser().parse(request)
            print("Message from PUT",request)
            employee = Employees.objects.get(EmployeesID=employee_data["EmployeesID"])
            employee_serailizer = EmployeesSerailizer(employee,data=employee_data)
            if employee_serailizer.is_valid():
                employee_serailizer.save()
                return JsonResponse("Update Successfully",safe=False)
            return JsonResponse("Fails to Update",safe=False)
        except Exception as e:
            print("Error message in PUT : " , e )
   
    elif request.method == "DELETE":
        try:
            print('Entery in Delete Method')
            employee = Employees.objects.get(EmployeesID=id)
            employee.delete()
            return JsonResponse("Delete Successfully",safe=False)
        except Exception as e:
            print("Error message in Delete : " , e )        