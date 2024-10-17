from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to display in the list view
    list_filter = ('author', 'publication_year')  # Filters on the right side
    search_fields = ('title', 'author')  # Search functionality for the title and author

admin.site.register(Book, BookAdmin)  # Register the model with the custom admin class
