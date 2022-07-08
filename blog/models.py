# pylint: disable=missing-module-docstring
from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse

from ckeditor.fields import RichTextField
# Create your models here.


class Post(models.Model):
    """
    Schema for making blog posts
    """
    title = models.CharField(max_length=100)
    content = RichTextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=CASCADE, null=False)
    time = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    is_reported = models.BooleanField(default=False)

    def __str__(self):
        """
        this will show default view in admin panel
        """
        return '%s - %s' % (self.title, self.author)

    def get_absolute_url(self):
        """
        Render to home page after creation
        """
        return reverse("dashboard")


class Comment(models.Model):
    """
    Schema for comments on post
    """
    comment_content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    comment_post = models.ForeignKey(
        Post, on_delete=CASCADE, related_name="comment_post")
    comment_user = models.ForeignKey(
        User, on_delete=CASCADE, related_name="comment_user")
    parent = models.ForeignKey(
        'self', default=None, on_delete=CASCADE, related_name="reply")
    is_reported = models.BooleanField(default=False)
    file = models.FileField(null=True)

    def __str__(self):
        """
        this will show default view in admin panel
        """
        return '%s - %s' % (self.comment_content, self.comment_post)

    def get_absolute_url(self):
        """
        Render to home page after creation
        """
        return reverse("viewpost", kwargs={'pk': self.comment_post.id})


class Suggestion(models.Model):
    """
    Schema for suggestions on post
    """
    suggestion_content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    suggestion_post = models.ForeignKey(
        Post, on_delete=CASCADE, related_name="suggestion_post")
    suggestion_user = models.ForeignKey(
        User, on_delete=CASCADE, related_name="suggestion_user")
    reply = models.ForeignKey(
        'self', default=None, on_delete=CASCADE, related_name="suggestion_reply")
    status = models.CharField(max_length=20, null=True, default="suggested")

    def __str__(self):
        """
         this will show default view in admin panel
        """
        return '%s - %s' % (self.suggestion_content, self.suggestion_user)

    def get_absolute_url(self):
        """
        Render to home page after creation
        """
        return reverse("viewpost", kwargs={'pk': self.suggestion_post.id})


class Likes(models.Model):
    """
    Schema for likes reocrd
    """
    user = models.ForeignKey(User, on_delete=CASCADE,
                             related_name="user_likes")
    post = models.ForeignKey(Post, on_delete=CASCADE,
                             null=True, related_name="post_likes")
    comment = models.ForeignKey(Comment, on_delete=CASCADE,
                                null=True, related_name="comment_likes")
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
         this will show default view in admin panel
        """
        return '%s - %s' % (self.post, self.user)

    def get_absolute_url(self):
        """
        Render to home page after creation
        """
        return reverse("home")
