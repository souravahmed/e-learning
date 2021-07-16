from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .manager import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    
    EDUCATOR = 2
    LEARNER = 3
    
    ROLE_CHOICES = (
        (EDUCATOR, 'Educator'),
        (LEARNER, 'Learner')
    )
    
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    first_name = models.CharField(verbose_name='first name', max_length=255)
    last_name = models.CharField(verbose_name='last name', max_length=255)
    mobile_number = models.CharField(verbose_name='mobile number', max_length=11)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    role = models.PositiveSmallIntegerField(choices= ROLE_CHOICES)
    last_login = models.DateTimeField(auto_now=timezone.now())
    date_joined = models.DateTimeField(auto_now_add=timezone.now())
    USERNAME_FIELD = 'email'
    objects = UserManager()
    
    def __str__(self):
        return self.email