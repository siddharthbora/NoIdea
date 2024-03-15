from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Doctors(models.Model):  # extended user model
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    reg_id = models.CharField(max_length=20, verbose_name="Reg. ID")
    phone = models.IntegerField(default=0)
    specialization = models.CharField(default='MD', max_length=25)