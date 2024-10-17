from django.shortcuts import render

# Create your views here.

from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, render
from .models import Book
from .forms import ExampleForm


@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Your editing logic here
    return render(request, 'bookshelf/edit_book.html', {'book': book})

from django.shortcuts import render
from .models import Book
from django.contrib.auth.decorators import permission_required

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()  # Retrieve all book instances
    return render(request, 'bookshelf/book_list.html', {'books': books})


from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

from django.contrib.auth.decorators import permission_required

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    # Your logic here
    pass

