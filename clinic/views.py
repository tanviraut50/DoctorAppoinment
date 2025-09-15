from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from .models import Doctor
from .forms import DoctorForm

def home(request):
    doctors = Doctor.objects.select_related("user").all()
    return render(request, "clinic/home.html", {"doctors": doctors})

def is_doctor(user): return hasattr(user, "doctor_profile") or getattr(user.profile, "role", "") == "DOCTOR"

@login_required
def doctor_detail(request, pk):
    doc = get_object_or_404(Doctor, pk=pk)
    return render(request, "clinic/doctor_detail.html", {"doctor": doc})

@login_required
@user_passes_test(is_doctor)
def doctor_create_or_edit(request):
    # create or edit the current user's doctor profile (CRUD: create/update)
    try:
        instance = request.user.doctor_profile
    except Doctor.DoesNotExist:
        instance = None
    if request.method == "POST":
        form = DoctorForm(request.POST, instance=instance)
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.user = request.user
            doctor.save()
            return redirect("doctor_detail", pk=doctor.pk)
    else:
        form = DoctorForm(instance=instance)
    return render(request, "clinic/doctor_form.html", {"form": form})
