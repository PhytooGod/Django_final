from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Book, Journal
admin.site.register(Book)
admin.site.register(Journal)