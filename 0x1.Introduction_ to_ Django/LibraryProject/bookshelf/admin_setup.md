# Admin Setup for Book Model

**Step 1:** Open `bookshelf/admin.py`.

**Step 2:** Register the `Book` model with the following code:
```python
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)
