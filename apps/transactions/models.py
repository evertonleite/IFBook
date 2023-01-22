from django.db import models
from apps.books.models import Book
from apps.account.models import User

# Create your models here.
class Transaction(models.Model):
    STATUS_CHOICES = (
        ("1", "Compra"),
        ("2", "Venda"),
    )
    timetable = models.DateTimeField(verbose_name="Horário", auto_now_add=True)
    type = models.CharField(
        verbose_name="Tipo",
        max_length=1,
        choices=STATUS_CHOICES,
        blank=False,
        null=False,
    )
    user = models.ForeignKey(User, verbose_name="Vendedor", on_delete=models.CASCADE)

    def __str__(self):
        return self.type
