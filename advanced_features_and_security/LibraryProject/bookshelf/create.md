# Create a Book Instance

To create a new book instance, use the following code:

```python
from bookshelf.models import Book

# Creating a new Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Confirmation
print("Book created:", book.title, book.author, book.publication_year)
