from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name']  

class PostSerializer(serializers.ModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user')
    user_detail = UserSerializer(source='user', read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d at %H:%M:%S", read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'category', 'created_by', 'user_detail', 'created_at']
        read_only_fields = ['created_at', 'user_detail']
