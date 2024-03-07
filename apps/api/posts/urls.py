from django.urls import path
from .views import PostListAPIView, RecentCommentPostListAPIView, PostListOrderedByCreatedAt, CommentViewSet, PostCreateViewSet

urlpatterns = [
    path('', PostListAPIView.as_view(), name='post-list'),
    path('create/', PostCreateViewSet.as_view({'post': 'create'}), name='create-posts'),
    path('create-comment/', CommentViewSet.as_view({'post': 'create'}), name='craete-comment'),
    path('delete-comment/<uuid:pk>/', CommentViewSet.as_view({'delete': 'destroy'}), name='craete-comment'),
    path('recent-comments/', RecentCommentPostListAPIView.as_view(), name='recent-comment-posts'),
    path('ordered-by-created-at/', PostListOrderedByCreatedAt.as_view(), name='posts-ordered-by-created-at'),
]