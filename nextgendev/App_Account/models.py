from django.db import models

from django.utils import timezone
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_suparuser=models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    
    id=models.AutoField(primary_key=True)
    firstName=models.CharField( max_length=50,null=True,blank=True)
    lastName=models.CharField( max_length=50,null=True,blank=True)
    email=models.EmailField( max_length=50,unique=True)
    password=models.CharField(max_length=256)
    mobile=models.CharField( max_length=20,null=True,blank=True)
    otp=models.CharField(null=True,blank=True, max_length=6)
    image=models.ImageField( upload_to="userprofile", null=True,blank=True)
    created_at=models.DateTimeField( auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
