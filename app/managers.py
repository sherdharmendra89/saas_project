from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class CustomUserManager(BaseUserManager):

    def _create_user(self, username, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError(('The given username must be set'))
        user = self.model(username=username, is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username,  password=None, **extra_fields):
        return self._create_user(username, password, False, False, ' ',
                                 **extra_fields)

    def create_superuser(self, username,  password, **extra_fields):
        user = self._create_user(username,  password, True, True,
                                 **extra_fields)
        user.is_active = True
        user.save(using=self._db)
        return user