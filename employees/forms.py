from django import forms
from .models import Employees

class EmployeesForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = ['name', 'address', 'phone_number', 'email', 'description']

    def clean_phone_number(self):
        phone = self.cleaned_data['phone_number']
        if not phone.isdigit():
            raise forms.ValidationError("Phone number must be numeric, contains only digits.")
        return phone

    def __init__(self, *args, **kwargs):
        super(EmployeesForm, self).__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.fields['salary'].disabled = True
            self.fields['designation'].disabled = True