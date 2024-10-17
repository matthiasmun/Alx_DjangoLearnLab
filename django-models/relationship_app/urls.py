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

