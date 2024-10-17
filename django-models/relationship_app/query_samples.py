import os
import django

# Set up the Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Book, Library, Librarian, Author

def query_all_books_by_author(author_name):
    books = Book.objects.filter(author__name=author_name)
    return books

def list_all_books_in_library(library_id):
    library = Library.objects.get(id=library_id)
    return library.books.all()

def retrieve_librarian_for_library(library_id):
    librarian = Librarian.objects.get(library__id=library_id)
    return librarian

if __name__ == "__main__":
    # Example usages
    author_name = "Author Name"  # Replace with a valid author name
    print("Books by author:", query_all_books_by_author(author_name))

    library_id = 1  # Replace with a valid library ID
    print("Books in library:", list_all_books_in_library(library_id))

    print("Librarian for library:", retrieve_librarian_for_library(library_id))
