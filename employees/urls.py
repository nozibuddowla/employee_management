from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('add/', views.add_employee, name='add_employee'),
    path('update/<int:employee_id>/', views.update_employee, name="update_employee"),
    path('delete/<int:employee_id>/', views.delete_employee, name="delete_employee"),
]