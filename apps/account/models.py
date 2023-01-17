from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager



class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField("Nome", max_length=255)
    username = models.CharField(max_length=25, unique=True)
    email = models.EmailField("E-mail", max_length=255)
    balance = models.CharField("Saldo", max_length=255)
    phone = models.CharField("Telefone", max_length=50)
    
    is_staff = models.BooleanField("Administrador", default=False)
    is_active = models.BooleanField("Ativo", default=True)
    date_joined = models.DateTimeField("Data de Entrada", auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = "username"
    
    def __str__(self):
        return self.name
    
class Adress(models.Model):
    street = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    cep = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    complement = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.city
    
    
    
