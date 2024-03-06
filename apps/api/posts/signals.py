from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Comment, Post

@receiver(post_delete, sender=Comment)
def delete_post_if_no_comments(sender, instance, **kwargs):
    post = instance.post
    if post.comments.count() == 0:
        post.delete()
