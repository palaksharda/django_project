# blogging/views.py
from rest_framework.decorators import api_view
from blogging.models import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status

from .serializers import PostSerializer, UserSerializer


@csrf_exempt
@api_view(['GET', 'POST'])
def post_create(request):
    if request.method == "GET":
        posts = Post.objects.all()
        serialized_data = PostSerializer(instance=posts, many=True, context={"request": request}).data
        return Response(
            data=
            {
                "message": "List of post records", 
                "data": serialized_data
            }
        )

    if request.method == "POST":
        post_serializer = PostSerializer(data=request.data, context={"request": request})
        post_serializer.is_valid(raise_exception=True)
        post = post_serializer.save()
        serialized_data = PostSerializer(instance=post, context={"request": request}).data
        return Response(
            data=
            {
                "message": "New post record created", 
                "data": serialized_data
            },
            status=status.HTTP_201_CREATED
            )

