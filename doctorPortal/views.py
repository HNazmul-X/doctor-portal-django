from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from doctorPortal.form import addAppointmentForm, addDoctorForm, addPatientForm
from doctorPortal.models import DoctorsModel, PateintModel



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
    return render(req, "pages/dashboard.html")


###############################################
# Patient Related view
###############################################
@login_required(login_url="/login")
def seeAllPatient(req):
    print(req.user)
    if req.user.is_authenticated:
        allpatients = PateintModel.objects.all()
        allpatients = reversed(allpatients)
        return render(req, "pages/seeAllPatient.html", {"patients": allpatients})
    else:
        return redirect("/login")


@login_required(login_url="/login")
def addPatient(req):
    form = addPatientForm(req.POST or None)
    print(req.POST)
    if req.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("addPatient")

    return render(req, "pages/addPatient.html", {"form": form})


@login_required(login_url="/login")
def delPatient(req,patientId):
    patient = PateintModel.objects.get(pk=patientId)
    patient.delete()
    return redirect("allPatient")


###############################################
# doctor Related Views
###############################################
@login_required(login_url="/login")
def addDoctor(req):
    form = addDoctorForm(req.POST or None)
    if req.method=="POST":
        if form.is_valid():
            form.save()
            return redirect("allDoctor")
    return render(req,"pages/doctor/addDoctor.html",{"form":form})


@login_required(login_url="/login")
def allDoctor(req):
    doctors = DoctorsModel.objects.all()
    return render(req, "pages/doctor/allDoctor.html",{"doctors":doctors})


@login_required(login_url="/login")
def delDoctor(req,doctorId):
    doctor = DoctorsModel.objects.get(pk=doctorId)
    doctor.delete()
    return redirect("allDoctor")


###############################################
# Appointment Related Views
###############################################
@login_required(login_url="/login")
def addAppointment(req):
    form = addAppointmentForm(req.POST or None)
    print(form)
    if req.method =="POST":
        if form.is_valid():
            form.save()
            return redirect(allAppointment)
    else:
        return render(req,"pages/appointment/addAppointment.html",{"form":form})

@login_required(login_url="/login")
def allAppointment(req):
    pass


@login_required(login_url="/login")
def delAppointment(req):
    pass


