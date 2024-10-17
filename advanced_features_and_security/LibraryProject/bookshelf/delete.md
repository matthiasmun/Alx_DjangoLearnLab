
### `delete.md`
```markdown
# Delete a Book Instance

To delete a book instance, use the following code:

```python
from bookshelf.models import Book

# Retrieving the Book instance to delete
book_to_delete = Book.objects.get(title="1984")

# Deleting the Book instance
book_to_delete.delete()

# Confirmation
try:
    Book.objects.get(title="1984")
except Book.DoesNotExist:
    print("Book deleted successfully.")
