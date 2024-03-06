from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from core.common import BaseModel
from constants.constant import HUNDRED

class Post(BaseModel):
    """
    Model representing a post.

    Attributes:
        title (str): The title of the post.
        author (User): The user who created the post.
        content (str): The content of the post.
        created_at (datetime): The date and time when the post was created.
    """
    title = models.CharField(_("Title"), max_length=HUNDRED, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Author"))
    content = models.TextField(_("Content"))
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    
    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

class Comment(BaseModel):
    """
    Model representing a comment on a post.

    Attributes:
        post (Post): The post on which the comment is made.
        author (User): The user who made the comment.
        content (str): The content of the comment.
        publication_date (datetime): The date and time when the comment was published.
    """
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments', verbose_name=_("Post"))
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Author"))
    content = models.TextField(_("Content"))
    publication_date = models.DateTimeField(_("Publication Date"), auto_now_add=True)

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
        ordering = ["-publication_date"]

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"
