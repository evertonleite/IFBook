from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(
        verbose_name="Nome", max_length=255, null=False, blank=False
    )
    username = models.CharField(verbose_name="Username", max_length=25, unique=True)
    email = models.EmailField(
        verbose_name="E-mail", max_length=255, null=False, blank=False
    )
    balance = models.CharField(verbose_name="Saldo", max_length=255)
    phone = models.CharField(
        verbose_name="Telefone", max_length=50, null=False, blank=False
    )

    is_staff = models.BooleanField(verbose_name="Administrador", default=False)
    is_active = models.BooleanField(verbose_name="Ativo", default=True)
    date_joined = models.DateTimeField(
        verbose_name="Data de Entrada", auto_now_add=True
    )

    objects = UserManager()

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.name


class Adress(models.Model):
    street = models.CharField(verbose_name="Rua", max_length=255)
    number = models.CharField(verbose_name="Número", max_length=20)
    district = models.CharField(verbose_name="Bairro", max_length=50)
    cep = models.CharField(verbose_name="CEP", max_length=12)
    city = models.CharField(verbose_name="Cidade", max_length=50)
    state = models.CharField(verbose_name="Estado", max_length=20)
    complement = models.CharField(verbose_name="Complemento", max_length=255)
    user = models.ForeignKey(User, verbose_name="Usuário", on_delete=models.CASCADE)

    def __str__(self):
        return self.city
