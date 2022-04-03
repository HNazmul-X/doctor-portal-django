from django.contrib import admin
from .models import UserModel,PateintFeestatus,PateintModel,DoctorsModel,AppointmentModel

# Register your models here.
admin.site.register(UserModel)
admin.site.register(PateintModel)
admin.site.register(PateintFeestatus)
admin.site.register(DoctorsModel)
admin.site.register(AppointmentModel)