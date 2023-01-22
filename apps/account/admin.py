from django.contrib import admin
from apps.account.models import User, Adress

# Register your models here.
admin.site.register(User)
admin.site.register(Adress)
