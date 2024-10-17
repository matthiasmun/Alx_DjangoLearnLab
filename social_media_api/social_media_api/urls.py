from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),  # Ensure this points to the correct URL config for accounts
    path('api/posts/', include('posts.urls')),  # Ensure this points to the correct URL config for posts
    path('api-auth/', include('rest_framework.urls')),  # Include DRF auth URLs
]
