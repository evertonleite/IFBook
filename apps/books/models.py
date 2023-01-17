from django.db import models
from apps.account.models import User

class Book(models.Model):
    STATUS_CHOICES = (
        ("1", "Novo"),
        ("2", "Usado"),
        ("3", "Seminovo"),
    )
    
    name = models.CharField(max_length=255)
    qtd_pages = models.CharField(max_length=255)
    book_cover = models.ImageField(upload_to ='images/')
    status_book = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=False, null=False)
    note = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
    synopsis = models.CharField(max_length=255)
    publishing_company = models.CharField(max_length=255)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    qtd_books = models.IntegerField(default=0)
    books = models.ManyToManyField(Book)
    
    
    
    