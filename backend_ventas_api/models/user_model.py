from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

"""
class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    name_user = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=50, unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    # roles = models.ManyToManyField('Role', through='UserRole', related_name='users')

    def __str__(self):
        return self.name_user
    class Meta:
        db_table = 'user'
"""

class UserManager(BaseUserManager):
    def create_user(self, name_user, email, password=None, **extra_fields):
        if not name_user:
            raise ValueError("El nombre de usuario debe ser proporcionado")
        if not email:
            raise ValueError("El email debe ser proporcionado")
        
        email = self.normalize_email(email)
        user = self.model(name_user=name_user, email=email, **extra_fields)
        user.set_password(password)  # Cifra la contraseña
        user.save(using=self._db)
        return user

   
    def create_superuser(self, name_user, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(name_user, email, password, **extra_fields)

class User(AbstractBaseUser):
    id_usuario = models.AutoField(primary_key=True)
    name_user = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'name_user'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.name_user
    
    def has_perm(self, perm, obj=None):

        if self.is_superuser:
            return True 

    def has_module_perms(self, app_label):
        if self.is_superuser:
            return True 

    class Meta:
        db_table = 'user'
