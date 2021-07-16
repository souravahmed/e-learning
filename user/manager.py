from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_field):
        if not email:
            raise ValueError('User must have an email address')
        
        user = self.model(email=self.normalize_email(email), **extra_field)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password=None, **extra_field):
        extra_field.setdefault('is_superuser', True)
        extra_field.setdefault('is_staff', True)
        extra_field.setdefault('role', 0)
        
        if extra_field.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        
        if extra_field.get('is_superuser') is not True:
            raise ValueError('SuperUser must be assigned to is_superuser=True')
        
        return self.create_user(email, password, **extra_field)