from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmployeesForm
from django.db import IntegrityError
from .models import Employees
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.
def index(request):
    employees = Employees.objects.all()
    return render(request, 'index.html', {'employees': employees})

@login_required
def add_employee(request):
    if request.method == 'POST':
        form = EmployeesForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('index')
            except IntegrityError:
                form.add_error('phone_number', 'This Phone number already exists')
                form.add_error('email', 'This Email already exists')
        else:
            return render(request, 'add_employee.html', {'form': form})
    else:
        form = EmployeesForm()

    return render(request, 'add_employee.html', {'form': form})

@login_required
def update_employee(request, employee_id):
    employee = get_object_or_404(Employees, pk = employee_id)

    if request.method == 'POST':
        form = EmployeesForm(request.POST, instance = employee)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, 'update_employee.html', {'form': form})
    else:
        form = EmployeesForm(instance = employee)

    return render(request, 'update_employee.html', {'form': form})

@login_required
def delete_employee(request, employee_id):
    employee = get_object_or_404(Employees, pk = employee_id)

    if request.method == 'POST':
        employee.delete()
        return redirect('index')
    
    return render(request, 'delete_employee.html', {'employee': employee})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'registration/register.html', {'form': form})
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})