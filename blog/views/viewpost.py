# pylint: disable=too-many-ancestors, no-member
from django.views.generic import DetailView
from blog.models import Comment, Post


class ViewPost(DetailView):
    """
    This class gives detail of each post when user select one
    """
    model = Post
    template_name = "viewpost.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pid = self.kwargs["pk"]
        context["post"] = Post.objects.get(id=pid)
        context["comments"] = Comment.objects.filter(comment_post__id=pid, parent=None)
        replies = Comment.objects.filter(comment_post__id=pid).exclude(parent=None)
        context["replies"] = replies
        return context
