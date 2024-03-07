from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import APIException
from .serializers import (
    PostSerializer,
    CommentSerializer,
    Post,
    Comment,
    PostCreateSerializer,
    CommentCreateSerializer,
)
from django.db.models import Max, Q
from django.db.models import Case, When, Value, BooleanField


class PostListAPIView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(title__isnull=False)


class RecentCommentPostListAPIView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        """
        Retrieve the 10 most relevant posts based on recent comments, prioritizing posts with comments and ordering them by the most recent comment date and post creation date.

        Returns:
            QuerySet: A queryset containing the 10 most relevant posts.

        Explanation:
        - Annotate each post with a boolean field 'has_comments' indicating whether the post has any associated comments.
        - Annotate each post with 'max_comment_date', representing the maximum publication date of comments associated with the post.
        - Order the queryset based on the following criteria:
            1. Posts without comments are listed first to fill any remaining portion.
            2. Posts with recent comments are prioritized, with those having the most recent comments listed first.
            3. If there are ties in the comment dates, posts are ordered by their creation date, with newer posts listed first.
        - Limit the queryset to the first 10 results to retrieve only the most relevant posts.
        """
        recent_comment_posts = (
            Post.objects.annotate(
                has_comments=Case(
                    When(comments__isnull=False, then=Value(True)),
                    default=Value(False),
                    output_field=BooleanField(),
                )
            )
            .annotate(max_comment_date=Max("comments__publication_date"))
            .order_by("-has_comments", "-max_comment_date", "-created_at")[:10]
        )
        return recent_comment_posts


class PostListOrderedByCreatedAt(generics.ListAPIView):
    """View to list posts ordered by creation date."""
    serializer_class = PostSerializer

    def get_queryset(self):
        """Get the queryset of posts ordered by creation date."""
        return Post.objects.order_by("-created_at")


class PostCreateViewSet(viewsets.ViewSet):
    """ViewSet for creating new posts."""
    def create(self, request):
        serializer = PostCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentViewSet(viewsets.ViewSet):
    """ViewSet for creating and deleting comments."""
    def create(self, request):
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            comment = Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            return Response(
                {"error": "Comment not found."}, status=status.HTTP_404_NOT_FOUND
            )

        comment.delete()
        return Response(
            {"message": "Comment deleted successfully."},
            status=status.HTTP_204_NO_CONTENT,
        )
