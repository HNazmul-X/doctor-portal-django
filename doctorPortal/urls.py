from django.urls import path
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
    path("delAppointment/<slug:appointmentID>",views.delAppointment,name="delAppointment"),

    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("", views.dashboard, name="dashboard")
]
