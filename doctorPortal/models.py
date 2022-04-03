from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManager
import uuid

# Create your models here.

class UserModel(AbstractBaseUser):
    email = models.EmailField(max_length=150,unique=True)
    fullname = models.CharField(verbose_name="Full Name",max_length=140)
    username = models.CharField(verbose_name="User Name",max_length=100)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    object = UserManager()

    def __str__(self):
        return self.email


    def has_perm(self,perm,obj=None):
        return True
    
    def has_module_perms(self,app_label):
        return True


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
    salary = models.IntegerField(verbose_name="salary of Doctor")

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


