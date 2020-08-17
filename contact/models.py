from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,BaseUserManager,PermissionsMixin
)

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,email,password=None,is_staff=False,is_admin=False,is_active=True,is_superuser=True):
        if not email:
            raise ValueError("User must have email address")

        if not password:
            raise ValueError("User must have password")

        user = self.model(
            email = self.normalize_email(email)
        )
        user.set_password(password)
        user.staff = is_staff
        user.active = is_active
        user.admin = is_admin
        user.superuser = is_superuser
        user.save(self._db)
        return user

    def create_staffuser(self,email,password=None):
        user = self.create_user(email,password=password,is_staff=True)
        return user
    def create_superuser(self,email,password=None):
        user = self.create_user(
            email,
            password=password, 
            is_staff=True,
            is_admin=True,
        )
        return user


class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=255,unique= True)
    active = models.BooleanField(default=True)
    staff=models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    superuser = models.BooleanField(default=False)
    

    USERNAME_FIELD = 'email'
    REQUIREDE_FIELDS = []
    def  __str__(self):
        return self.email

    def  get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_active(self):
        return self.active
    @property
    def is_admin(self):
        return self.admin
    @property
    def is_superuser(self):
        return self.superuser

    objects = UserManager()


class Contact(models.Model):
    fullname = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    subject =models.CharField(max_length=120)
    body = models.CharField(max_length=5000)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
