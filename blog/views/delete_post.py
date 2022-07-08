# pylint: disable=no-member, too-many-ancestors, line-too-long

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import DeleteView
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from blog.models import Post, User

class DeletePost(LoginRequiredMixin, DeleteView):
    """
    This will ask user for confirmation to delete any post
    """
    model = Post
    success_url = reverse_lazy("dashboard")
    template_name = "dashboard.html"

    def get(self, request, *args, **kwargs):
        try:
            pid = self.kwargs["pk"]
            post = Post.objects.get(id=pid)
            if User.objects.filter(pk=self.request.user.id, groups__name="Moderator").exists() or self.request.user == post.author:
                post.delete()
                messages.warning(request, "Post has been deleted successfully...")
            else:
                messages.warning(request, "Permission denied")
            return render(request, self.template_name)
        except ObjectDoesNotExist:
            raise Http404
