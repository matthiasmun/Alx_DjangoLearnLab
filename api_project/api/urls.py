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

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Add this line
]

