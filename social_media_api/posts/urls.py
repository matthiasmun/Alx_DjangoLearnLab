from django.urls import path
from .views import YourPostViewSet  # Change this to your actual viewset

urlpatterns = [
    path('', YourPostViewSet.as_view(), name='post-list'),
]

# posts/urls.py
from django.urls import path
from .views import LikePostView

urlpatterns = [
    path('<int:pk>/like/', LikePostView.as_view({'post': 'create', 'delete': 'destroy'}), name='like-post'),
]

# notifications/urls.py
from django.urls import path
from .views import NotificationViewSet

urlpatterns = [
    path('', NotificationViewSet.as_view({'get': 'list'}), name='notifications'),
]

# social_media_api/urls.py
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/posts/', include('posts.urls')),
    path('api/notifications/', include('notifications.urls')),  # Include notifications URLs
]
