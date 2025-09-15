from django.contrib import admin
from django.urls import path, include
from clinic.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),  # login, logout, password reset
    path("clinic/", include("clinic.urls")),
    path("appointments/", include("appointments.urls")),
]
