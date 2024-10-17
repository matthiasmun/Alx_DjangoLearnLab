from rest_framework import generics  # Add this line to import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):  # Correct usage of generics.ListAPIView
    queryset = Book.objects.all()
    serializer_class = BookSerializer
