from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_admin=models.BooleanField('Is_admin',default=False)
    is_patient=models.BooleanField('Is_patient',default=False)
    is_doctor=models.BooleanField('Is_doctor',default=False)
    Profile_pic=models.ImageField('Profile_pic',upload_to='img/',null=True, blank=True)
   