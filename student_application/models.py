# student_application/models.py

from django.db import models
from django.contrib.auth.models import User
from django.db import models



class Student_Info(models.Model):
    name = models.CharField(max_length=255, blank=False)
    age = models.IntegerField(blank=False)
    student_class = models.CharField(max_length=255, blank=False)
    tamilmarks = models.IntegerField(default=0)
    englishmarks = models.IntegerField(default=0) 
    sciencemarks = models.IntegerField(default=0)
    mathsmarks = models.IntegerField(default=0)
    socialmarks = models.IntegerField(default=0)

class login_page(models.Model):
    username = models.CharField(max_length=255, blank=False)                                                                                                                               
    password =models.CharField(max_length=255, blank=False)
   
class register_page(models.Model):
    first_name = models.CharField(max_length=255, blank=False)   
    last_name = models.CharField(max_length=255, blank=False)
    username = models.CharField(max_length=255, blank=False)
    password = models.CharField(max_length=255, unique=True, blank=False)

