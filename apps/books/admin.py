from django.contrib import admin
from apps.books.models import Book, Category, Cart

# Register your models here.
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Cart)