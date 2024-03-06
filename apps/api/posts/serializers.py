from rest_framework import serializers
from .models import Post, Comment
from users.models import User
from uuid import UUID

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'publication_date']

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    comments_count = serializers.SerializerMethodField()
    
    def get_comments_count(self, obj):
        return obj.comments.count()

    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'content', 'created_at', 'comments_count', 'comments']

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at']
        
    # def create(self, validated_data):
    #     author_id = validated_data.pop('author')
    #     print(type(author_id.id),'------------------------------------------------')
    #     try:
    #         author = User.objects.get(id=author_id)
    #     except User.DoesNotExist:
    #         raise serializers.ValidationError("Invalid author ID")

    #     validated_data['author'] = author
    #     return super().create(validated_data)

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','post', 'content', 'author', 'publication_date']