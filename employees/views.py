from django.shortcuts import render, redirect
from .forms import EmployeesForm

# Create your views here.
def add_employee(request):
    if request.method == 'POST':
        form = EmployeesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EmployeesForm()

    return render(request, 'add_employee.html', {'form': form})