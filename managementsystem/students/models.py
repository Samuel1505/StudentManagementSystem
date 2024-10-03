from django.db import models
from django.urls import reverse

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = (
        ('Male','Male'),
        ('Female','Female'),
        ('p','Prefer Not To Say'),  
    )
    gender = models.CharField(choices = gender,max_length=10)
    mat_number = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=255, unique=True)


    def get_absolute_url(self):
        return reverse("home")