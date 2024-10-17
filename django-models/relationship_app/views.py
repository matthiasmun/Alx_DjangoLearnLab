from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Book

def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

from django.views.generic import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'bookshelf/register.html', {'form': form})

from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    # Logic for admin view
    return render(request, 'bookshelf/admin_view.html')

# Similar for librarian_view and member_view


from django.contrib.auth.decorators import permission_required

@permission_required('bookshelf.can_add_book')
def add_book(request):
    # Logic to add a book
    return render(request, 'bookshelf/add_book.html')



