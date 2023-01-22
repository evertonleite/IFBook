from django.db import models
from apps.account.models import User
from apps.transactions.models import Transaction


class Book(models.Model):
    STATUS_CHOICES = (
        ("1", "Novo"),
        ("2", "Usado"),
        ("3", "Seminovo"),
    )

    name = models.CharField(verbose_name="Nome", max_length=255, blank=True)
    quantity_pages = models.CharField(verbose_name="Quantidade de Pg.", max_length=255)
    book_cover = models.ImageField(verbose_name="Capa", upload_to="images/")
    status_book = models.CharField(
        verbose_name="Status",
        max_length=1,
        choices=STATUS_CHOICES,
        blank=False,
        null=False,
    )
    note = models.CharField(verbose_name="Observação", max_length=255)
    year = models.CharField(verbose_name="Ano", max_length=255)
    price = models.CharField(verbose_name="Preço", max_length=255)
    quantity = models.CharField(verbose_name="Quantidade", max_length=255)
    synopsis = models.CharField(verbose_name="Sinopse", max_length=255)
    publishing_company = models.CharField(verbose_name="Editora", max_length=255)
    category = models.ForeignKey(
        "Category", verbose_name="Categoria", on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, verbose_name="Usuário", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(verbose_name="Nome", max_length=255)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.OneToOneField(
        User, verbose_name="Usuário", on_delete=models.SET_NULL, null=True
    )
    quantity_books = models.CharField(verbose_name="Quantidade", default=0)


# Tabela auxiliar para relação de N pra N livros e carrinho
class Book_Cart(models.Model):
    book = models.ForeignKey(Book, verbose_name="Livro", on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, verbose_name="Carrinho", on_delete=models.CASCADE)
    quantity_books = models.CharField(max_length=255)


# Tabela auxiliar para relação de N pra N livros e transações
class Book_Transaction(models.Model):
    book = models.ForeignKey(Book, verbose_name="Livro", on_delete=models.CASCADE)
    transaction = models.ForeignKey(
        Transaction, verbose_name="Transação", on_delete=models.CASCADE
    )
    quantity_books = models.CharField(verbose_name="Quantidade", default=0)
