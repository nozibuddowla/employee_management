from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_employee, name='add_employee'),
    path('update/<int:employee_id>/', views.update_employee, name="update_employee"),
]