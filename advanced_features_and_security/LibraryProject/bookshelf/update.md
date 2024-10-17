
### `update.md`
```markdown
# Update a Book Instance

To update an existing book instance, use the following code:

```python
from bookshelf.models import Book

# Retrieving the Book instance to update
book_to_update = Book.objects.get(title="1984")

# Updating the author and publication year
book_to_update.author = "George Orwell"
book_to_update.publication_year = 1950  # Example of an updated year

# Saving the changes
book_to_update.save()

# Confirmation
print("Book updated:", book_to_update.title, book_to_update.author, book_to_update.publication_year)
