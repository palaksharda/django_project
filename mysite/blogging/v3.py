from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import PostSerializer, UserSerializer


class PostListAPIView(GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        post = self.get_queryset()
        serializer = self.serializer_class(post, many=True)
        return Response({
            "message": "Post retrieved successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    


class PostAPIView(GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get_object(self, post_id):
        try:
            return Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return None


    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            post = serializer.save()
            return Response({
                "message": "Post saved successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, post_id, *args, **kwargs):
        post = self.get_object(post_id)
        if not post:
            return Response({"message": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Post updated successfully",
                "data": serializer.data
            })
        return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, post_id, *args, **kwargs):
        post = self.get_object(post_id)
        if not post:
            return Response({"message": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(post)
        return Response({
            "message": "Post retrieved successfully",
            "data": serializer.data
        })


    def delete(self, request, post_id, *args, **kwargs):
        post = self.get_object(post_id)
        if not post:
            return Response({"message": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

        post.delete()
        return Response({
            "message": "Post deleted successfully",
        }, status=status.HTTP_204_NO_CONTENT)