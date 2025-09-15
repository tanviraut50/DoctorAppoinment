from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("user", "specialization", "fees")
    search_fields = ("user__username", "user__first_name", "user__last_name", "specialization")
    list_filter = ("specialization",)
