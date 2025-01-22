from django.shortcuts import render, redirect
from .forms import EmployeesForm
from django.db import IntegrityError

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