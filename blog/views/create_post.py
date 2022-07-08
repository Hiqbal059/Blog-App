# pylint: disable=too-many-ancestors
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from blog.models import Post
from blog.forms import PostForm


class CreatePost(LoginRequiredMixin, CreateView):
    """
    This class will handle the functionality to let user create new post
    """
    model = Post
    form_class = PostForm
    template_name = "addpost.html"
