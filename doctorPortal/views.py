from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from doctorPortal.form import addAppointmentForm, addDoctorForm, addPatientForm
from doctorPortal.models import AppointmentModel, DoctorsModel, PateintModel



###############################################
# authentication & Dashboard Related Views
###############################################

def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    else:
        if request.method == "POST":
            email = request.POST.get("email")
            password = request.POST.get("password")
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("dashboard")
        return render(request, "pages/login.html")


@login_required(login_url="/login")
def logout_view(req):
    logout(req)
    return redirect("login")

# Dashboard View


@login_required(login_url="/login")
def dashboard(req):
    totalPatient = PateintModel.objects.count()
    totalDoctor = DoctorsModel.objects.count()
    totalAppointment = AppointmentModel.objects.count()
    return render(req, "pages/dashboard.html",{"totalAppointment":totalAppointment,"totalDoctor":totalDoctor,"totalPatient":totalPatient})


###############################################
# Patient Related view
###############################################
@login_required(login_url="/login")
def seeAllPatient(req):
    if req.user.is_authenticated:
        allpatients = PateintModel.objects.all()
        allpatients = reversed(allpatients)
        return render(req, "pages/seeAllPatient.html", {"patients": allpatients})
    else:
        return redirect("/login")

@login_required(login_url="/login")
def addPatient(req):
    form = addPatientForm(req.POST or None)
    if req.user.is_admin:
        return redirect(seeAllPatient)
    else:
        if req.method == "POST":
            if form.is_valid():
                form.save()
                return redirect("allPatient")

        return render(req, "pages/addPatient.html", {"form": form})


@login_required(login_url="/login")
def delPatient(req,patientId):
    if req.user.is_admin:
        return redirect(seeAllPatient)
    else:
        patient = PateintModel.objects.get(pk=patientId)
        patient.delete()
        return redirect("allPatient")


###############################################
# doctor Related Views
###############################################
@login_required(login_url="/login")
def addDoctor(req):
    if req.user.is_admin:
        form = addDoctorForm(req.POST or None)
        if req.method=="POST":
            if form.is_valid():
                form.save()
                return redirect("allDoctor")
        return render(req,"pages/doctor/addDoctor.html",{"form":form})
    else:
        return redirect("/")


@login_required(login_url="/login")
def allDoctor(req):
    doctors = DoctorsModel.objects.all()
    return render(req, "pages/doctor/allDoctor.html",{"doctors":doctors})



@login_required(login_url="/login")
def updateDoctor(req,doctorId):
    if req.user.is_admin:
        doctor = DoctorsModel.objects.get(pk=doctorId)
        form = addDoctorForm(req.POST or None, instance=doctor)
        if not req.user.is_admin:
            return redirect("allDoctor")
        if req.method == "POST":
            if form.is_valid():
                form.save()
                return redirect(allDoctor)
        return render(req, "pages/doctor/updateDoctor.html", {"form": form})
    else:
        return redirect("allDoctor")


@login_required(login_url="/login")
def delDoctor(req,doctorId):
    if req.user.is_admin:
        doctor = DoctorsModel.objects.get(pk=doctorId)
        doctor.delete()
        return redirect("allDoctor")
    else:
        return redirect("allDoctor")


###############################################
# Appointment Related Views
###############################################
@login_required(login_url="/login")
def addAppointment(req):
    form = addAppointmentForm(req.POST or None)
    if req.user.is_admin:
        return redirect("/")
    if req.method =="POST":
        if form.is_valid():
            form.save()
            return redirect(allAppointment)
    return render(req,"pages/appointment/addAppointment.html",{"form":form})

@login_required(login_url="/login")
def allAppointment(req):
    appointments = AppointmentModel.objects.all()
    return render(req,"pages/appointment/allAppointment.html",{"appointments":appointments})


@login_required(login_url="/login")
def delAppointment(req,appointmentID):
    if req.user.is_admin:
        return redirect("allAppointment")
    appointment = AppointmentModel.objects.get(pk=appointmentID)
    appointment.delete()
    return redirect("allAppointment")

