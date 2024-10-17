from django.contrib import admin
from django.urls import path, include  # Add 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # This line includes the URLs from the 'api' app
]
