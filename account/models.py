from django.db import models
from django_countries.fields import CountryField    #country
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    image = models.ImageField('image', upload_to='profile_images/', null=True, blank=True)
    phone = models.CharField(max_length=30)
    country = CountryField()    #country


class Instagram(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100,blank=True)
    follower=models.CharField(max_length=30,blank=True)
    following=models.CharField(max_length=30,blank=True)






