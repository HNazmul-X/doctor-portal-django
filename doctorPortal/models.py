from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
import uuid

# Create your models here.

class UserModel(AbstractUser):
    email = models.EmailField(max_length=150,unique=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    object = UserManager()

class PateintFeestatus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.status


class PateintModel(models.Model):
     id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
     fullname = models.CharField(max_length=150)
     symptoms = models.CharField(max_length=100)
     age = models.IntegerField()
     feeStatus = models.ForeignKey(PateintFeestatus,on_delete=models.CASCADE)
     address = models.CharField(max_length=150)
     mobile = models.CharField(max_length=20)

     def __str__(self):
        return self.fullname

class DoctorsModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fullname = models.CharField(max_length=100)
    specialize = models.CharField(max_length=100)
    age = models.IntegerField()
    mobile = models.CharField(max_length=20)
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.fullname

class AppointmentModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pateint = models.ForeignKey(PateintModel,on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorsModel,on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.subject


