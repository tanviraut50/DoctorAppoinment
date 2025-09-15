from django.conf import settings
from django.db import models

class Doctor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="doctor_profile")
    specialization = models.CharField(max_length=120)
    fees = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    phone = models.CharField(max_length=20, blank=True)
    bio = models.TextField(blank=True)
    

    def __str__(self):
        return f"Dr. {self.user.get_full_name() or self.user.username} – {self.specialization}"
