# pylint: disable=too-many-ancestors

from django.views.generic import UpdateView
from blog.forms import PostForm
from blog.models import Post


class UpdatePost(UpdateView):
    """
    This class will provide the functionality to update the existing post
    """
    model = Post
    form_class = PostForm
    template_name = "editpost.html"
