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

relationship_app/list_books.html

relationship_app/library_detail.html

from django.views.generic.detail import DetailView

from django.contrib.auth import login

"views.register", "LogoutView.as_view(template_name=", "LoginView.as_view(template_name="]

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView

class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('book_list')  # Redirect to your desired page after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')

from django.contrib.auth.decorators import permission_required

@permission_required('relationship_app.can_add_book')
def add_book_view(request):
    # Your logic for adding a book
    return render(request, 'add_book.html')

@permission_required('relationship_app.can_change_book')
def edit_book_view(request, book_id):
    # Your logic for editing a book
    return render(request, 'edit_book.html')

@permission_required('relationship_app.can_delete_book')
def delete_book_view(request, book_id):
    # Your logic for deleting a book
    return render(request, 'delete_book.html')


