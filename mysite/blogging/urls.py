# urls.py
from django.urls import path
from .views import post_create
from .v3 import PostAPIView,PostListAPIView

urlpatterns = [
    path('posts/', post_create, name='post_create'),

    path('post/', PostAPIView.as_view(), name='post-create'),  # For POST method
    path('post/<int:post_id>/', PostAPIView.as_view(), name='post-retrieve-update-delete'),  # For GET, PUT, DELETE methods
     path('post/all/', PostListAPIView.as_view(), name='post-list'),
]
