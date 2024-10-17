from django.contrib import admin
from django.urls import path, include  # Add 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # This line includes the URLs from the 'api' app
]

from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Keep your previous list view
    path('', include(router.urls)),  # Include the router URLs
]
