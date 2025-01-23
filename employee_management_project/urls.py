from django.contrib import admin
from django.urls import path, include
from employees.views import index, register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("registration/", register, name="register"),
    path("registration/login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("", index, name="index"),
    path("employees/", include("employees.urls")),
]
