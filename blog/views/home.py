# pylint: disable=no-member, too-many-ancestors
from django.core.paginator import Paginator
from django.views.generic import ListView
from blog.models import Post


class Home(ListView, Paginator):
    """
    Class to handle home page view
    """
    paginate_by = 4
    model = Post
    template_name = "home.html"
    ordering = ["-time"]

    def get_queryset(self):
        queryset = Post.objects.filter(is_published=True).order_by("-time")
        return queryset
