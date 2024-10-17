
### `retrieve.md`
```markdown
# Retrieve a Book Instance

To retrieve a book instance from the database, use the following code:

```python
from bookshelf.models import Book

# Retrieving the Book instance by title
retrieved_book = Book.objects.get(title="1984")

# Displaying book details
print("Title:", retrieved_book.title)
print("Author:", retrieved_book.author)
print("Publication Year:", retrieved_book.publication_year)
