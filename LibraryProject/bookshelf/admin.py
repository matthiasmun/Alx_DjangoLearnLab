from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Display these fields in the admin list view
    search_fields = ('title', 'author')  # Enable search for these fields
    list_filter = ('publication_year',)  # Enable filtering by publication year

from django.contrib import admin
from .models import Book

# Register the Book model with the admin site
admin.site.register(Book)
