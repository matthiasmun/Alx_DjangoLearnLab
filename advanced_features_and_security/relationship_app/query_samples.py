import os
import django

# Set up the Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Book, Library, Librarian, Author

def query_all_books_by_author(author_name):
    # Retrieve the author instance
    try:
        author = Author.objects.get(name=author_name)
        # Query all books by this author
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return f"No author found with the name: {author_name}"

def list_all_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return f"No library found with the name: {library_name}"

def retrieve_librarian_for_library(library_name):
    try:
        # Corrected query to get the librarian for the specified library
        librarian = Librarian.objects.get(library__name=library_name)
        return librarian
    except Librarian.DoesNotExist:
        return f"No librarian found for the library: {library_name}"

if __name__ == "__main__":
    # Example usages
    author_name = "Author Name"  # Replace with a valid author name
    print("Books by author:", query_all_books_by_author(author_name))

    library_name = "Library Name"  # Replace with a valid library name
    print("Books in library:", list_all_books_in_library(library_name))

    print("Librarian for library:", retrieve_librarian_for_library(library_name))
