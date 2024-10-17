from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]

from django.urls import include, path

urlpatterns = [
    path('relationship/', include('relationship_app.urls')),
    # other paths...
]

from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),

]

# urls.py
from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    # Other paths can go here

]

urlpatterns = [
    path('admin/', admin_view, name='admin_view'),
    # Add other role views here
]

urlpatterns = [
    path('add-book/', add_book, name='add_book'),
    # Add other actions for edit/delete
]

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    # Other paths...
]

from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    # Other paths...
]

from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]


urlpatterns = [
    path('admin/', views.admin_view, name='admin_view'),
    # Other role-based views
]

urlpatterns = [
    path('librarian/', views.librarian_view, name='librarian_view'),
    # Other role-based views
]

path('member/', views.member_view, name='member_view'),


from . import views

urlpatterns = [
    path('add-book/', views.add_book_view, name='add_book'),
    path('edit-book/<int:book_id>/', views.edit_book_view, name='edit_book'),
    path('delete-book/<int:book_id>/', views.delete_book_view, name='delete_book'),
    # Other URL patterns
]

from django.urls import path
from . import views

urlpatterns = [
    # Views for role-based access
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),

    # Paths for adding and editing books
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
]


