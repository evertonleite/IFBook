from django.db import models
from apps.books.models import Book

# Create your models here.
class Transaction(models.Model):
    STATUS_CHOICES = (
        ("1", "Compra"),
        ("2", "Venda"),
    )
    timetable = models.DateField()
    type = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=False, null=False)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)
    
    def __str__(self):
        return self.type
    