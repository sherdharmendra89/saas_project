
import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import *
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class BaseModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, db_index=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

class CustomGroup(models.Model):
    # Add your custom group fields here
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CustomPermission(models.Model):
    # Add your custom permission fields here
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class User(AbstractBaseUser,  PermissionsMixin, BaseModel):
    username = models.CharField(max_length=40, unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login_at = models.DateTimeField('last login', null=True, blank=True)
    last_login_ip = models.CharField(max_length=255)
    
    source_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, default=1)
    source_id = models.PositiveIntegerField(default=1)
    content_object = GenericForeignKey('source_type', 'source_id') 
    
    

    USERNAME_FIELD = "username"

    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username 



