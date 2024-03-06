from django.urls import path
from .views import PostListAPIView, RecentCommentPostListAPIView, PostListOrderedByCreatedAt, CommentCreateViewSet, PostCreateViewSet

urlpatterns = [
    # API endpoint to list all posts with comments
    path('', PostListAPIView.as_view(), name='post-list'),

    # API endpoint to list posts based on recent comments
    path('create/', PostCreateViewSet.as_view({'post': 'create'}), name='create-posts'),
    path('create-comment/', CommentCreateViewSet.as_view({'post': 'create'}), name='craete-comment'),
    path('recent-comments/', RecentCommentPostListAPIView.as_view(), name='recent-comment-posts'),

    # API endpoint to list posts based on creation date
    path('ordered-by-created-at/', PostListOrderedByCreatedAt.as_view(), name='posts-ordered-by-created-at'),
]