from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    #patient Route
    path("allPatient/", views.seeAllPatient, name="allPatient"),
    path("addPatient/", views.addPatient, name="addPatient"),
    path("delPatient/<slug:patientId>", views.delPatient, name="delPatient"),

    #doctor Route
    path("addDoctor/", views.addDoctor, name="addDoctor"),
    path("allDoctor/", views.allDoctor, name="allDoctor"),
    path("delDoctor/<slug:doctorId>", views.delDoctor, name="delDoctor"),

    #appointment Route
    path("addAppointment/",views.addAppointment,name="addAppointment"),
    path("allAppointment/",views.allAppointment,name="allAppointment"),
    path("update-doctor/<slug:doctorId>",views.updateDoctor,name="updateDoctor"),
    path("delAppointment/<slug:appointmentID>",views.delAppointment,name="delAppointment"),

    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("", views.dashboard, name="dashboard")
]
