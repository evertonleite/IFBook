from django.db import models
# class User(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(max_length=200, unique=True)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=200)
#     is_staff = models.BooleanField(null=True)
#     is_superuser = models.BooleanField(null=True)

#     objects = UserManager()

#     USERNAME_FIELD = "username"

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    balance = models.CharField(max_length=255)
    adress = models.ForeignKey("Adress", on_delete=models.CASCADE)
    
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
    
    def __str__(self):
        return self.city
    
    
    
