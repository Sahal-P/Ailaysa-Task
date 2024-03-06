from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import APIException
from .serializers import PostSerializer, CommentSerializer, Post, Comment, PostCreateSerializer, CommentCreateSerializer


class PostListAPIView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(title__isnull=False)

class RecentCommentPostListAPIView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        # Get the IDs of posts with recent comments
        recent_comment_post_ids = Comment.objects.order_by('-publication_date').values_list('post_id', flat=True).distinct()[:10]
        # Return posts with recent comments
        return Post.objects.filter(id__in=recent_comment_post_ids)

class PostListOrderedByCreatedAt(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.order_by('-created_at')


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_destroy(self, instance):
        instance.delete()
        # Check if the post has no comments left and delete it
        if instance.post.comments.count() == 0:
            instance.post.delete()

class PostCreateViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = PostCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentCreateViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)