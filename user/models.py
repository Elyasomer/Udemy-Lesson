from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(max_length=254)
    user_img = models.ImageField(null=True,blank=True)
    phone = models.CharField(max_length=100)
