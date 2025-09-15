from django.urls import path
from .views import doctor_detail, doctor_create_or_edit
urlpatterns = [
    path("me/", doctor_create_or_edit, name="doctor_edit"),
    path("<int:pk>/", doctor_detail, name="doctor_detail"),
]
