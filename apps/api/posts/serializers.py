from rest_framework import serializers
from .models import Post, Comment
from users.models import User
from uuid import UUID

class CommentSerializer(serializers.ModelSerializer):
    """Serializer for Comment model."""
    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'publication_date']

class PostSerializer(serializers.ModelSerializer):
    """Serializer for Post model."""
    comments = CommentSerializer(many=True, read_only=True)
    comments_count = serializers.SerializerMethodField()
    
    def get_comments_count(self, obj):
        """Get the count of comments associated with the post."""
        return obj.comments.count()

    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'content', 'created_at', 'comments_count', 'comments']

class PostCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating a new Post."""
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at']
        

class CommentCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating a new Comment."""
    class Meta:
        model = Comment
        fields = ['id','post', 'content', 'author', 'publication_date']