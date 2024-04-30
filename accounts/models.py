from django.db import models
from enum import Enum
#import abstractuser
from django.contrib.auth.models import AbstractUser

choices = [('doctor', 'doctor'), ('patient', 'patient')]

class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    user_type = models.CharField(max_length=10, choices = choices)
    