from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmployeesForm
from django.db import IntegrityError
from .models import Employees

# Create your views here.
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
        form = EmployeesForm()

    return render(request, 'add_employee.html', {'form': form})

def update_employee(request, employee_id):
    employee = get_object_or_404(Employees, pk = employee_id)

    if request.method == 'POST':
        form = EmployeesForm(request.POST, instance = employee)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EmployeesForm(instance = employee)

    return render(request, 'update_employee.html', {'form': form})