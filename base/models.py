from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    admission_number= models.IntegerField(null=True)
    dob = models.DateField(null=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    BATCH_CHOICES = (
        ('A', 'B22ECA'),
        ('B', 'B22ECB'),
    )
    ROLES = (
        ('S', 'Student'),
        ('A', 'Advisor'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default="A")
    batch = models.CharField(max_length=7,choices=BATCH_CHOICES,default="M")
    role = models.CharField(max_length=7,choices=ROLES,default="S")
    # add additional fields in here

    def __str__(self):
        return self.username