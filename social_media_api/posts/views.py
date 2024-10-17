from django.shortcuts import render

# Create your views here.
from .serializers import UserSerializer

from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly  # Custom permission

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # Automatically set the author to the logged-in user

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # Automatically set the author to the logged-in user


# posts/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Post, Like
from rest_framework.permissions import IsAuthenticated

class LikePostView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request, pk=None):
        post = self.get_object(pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if created:
            # Optionally create a notification
            Notification.objects.create(
                recipient=post.user,
                actor=request.user,
                verb='liked your post',
                target=post
            )
            return Response({'status': 'liked'}, status=status.HTTP_201_CREATED)
        return Response({'status': 'already liked'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        post = self.get_object(pk)
        like = Like.objects.filter(user=request.user, post=post)
        if like.exists():
            like.delete()
            return Response({'status': 'unliked'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'status': 'not liked'}, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        return Post.objects.get(pk=pk)

# notifications/views.py
from rest_framework import viewsets
from .models import Notification
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class NotificationViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by('-timestamp')

    def list(self, request):
        notifications = self.get_queryset()
        return Response({'notifications': notifications})

# notifications/urls.py
from django.urls import path
from .views import NotificationViewSet

urlpatterns = [
    path('', NotificationViewSet.as_view({'get': 'list'}), name='notifications'),
]


# posts/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from .models import Post, Like
from notifications.models import Notification
from rest_framework.permissions import IsAuthenticated

class LikePostView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)  # Use get_object_or_404
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if created:
            # Create a notification for the user
            Notification.objects.create(
                recipient=post.user,
                actor=request.user,
                verb='liked your post',
                target=post
            )
            return Response({'status': 'liked'}, status=status.HTTP_201_CREATED)
        return Response({'status': 'already liked'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)  # Use get_object_or_404
        like = Like.objects.filter(user=request.user, post=post)
        if like.exists():
            like.delete()
            return Response({'status': 'unliked'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'status': 'not liked'}, status=status.HTTP_400_BAD_REQUEST)


