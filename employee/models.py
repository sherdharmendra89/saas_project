from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.
from app.models import BaseModel, User

class Employee(BaseModel):
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    dob = models.DateField(auto_now=True)
    pan = models.CharField(max_length=10,blank=True)
    uid = models.CharField(max_length=12, blank=True)
    date_of_joining = models.DateField(auto_now=True)
    date_of_releiving = models.DateField(auto_now=True)
    professional_email = models.EmailField()
    professional_contact = models.CharField(max_length=15)
    user = GenericRelation(User)


    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'