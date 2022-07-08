# pylint: disable=no-member

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from blog.models import Comment, Post, User, Likes


class Dashboard(LoginRequiredMixin, TemplateView):
    """
    User dashboard will be handled through this class
    """
    success_url = 'dashboard'
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        if User.objects.filter(pk=self.request.user.id, groups__name="Moderator").exists():
            context = super().get_context_data(**kwargs)
            context["posts"] = Post.objects.filter(is_published=False).order_by('-time')
            context["reported_posts"] = Post.objects.filter(is_reported=True).order_by('-time')
            context["moderator"] = True
        else:
            user = self.request.user
            context = super().get_context_data(**kwargs)
            context['posts'] = Post.objects.filter(author=user, is_published=True).order_by('-time')
            context['pending_posts'] = Post.objects.filter(
                author=user, is_published=False).order_by('-time')
            context['comments'] = Comment.objects.filter(
                comment_post__author=user).order_by('-time')
            context['likes'] = Likes.objects.filter(post__author=user).order_by('-time')
        return context
