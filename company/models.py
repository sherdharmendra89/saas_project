from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models
from app.models import BaseModel, User
# from django.contrib.postgres.fields import CICharFielde
from django.contrib.contenttypes.fields import GenericRelation



class Company(BaseModel):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='images/')
    website = models.CharField(max_length=255)
    subdomain = models.CharField(max_length=100)
    domain = models.CharField(max_length=255)
    user = GenericRelation(User)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'