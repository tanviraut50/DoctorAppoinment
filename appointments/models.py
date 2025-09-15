from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="patient_appointments")
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="doctor_appointments")
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default="09:00:00")
  

    def __str__(self):
        return f"{self.patient} with {self.doctor} on {self.date} at {self.time}"
