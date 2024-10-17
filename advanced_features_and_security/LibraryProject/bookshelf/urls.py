from django.urls import path
from .views import book_list

urlpatterns = [
    path('books/', book_list, name='book_list'),  # Route to book_list view
    # Other paths can go here if you plan to add more views later
]
