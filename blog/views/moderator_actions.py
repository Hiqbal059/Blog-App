# pylint: disable=no-member

from django.contrib.auth.mixins import LoginRequiredMixin
from django import views
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls.base import reverse
from blog.models import Post, User

class ModeratorActions(LoginRequiredMixin, views.View):
    """
    This class handles the actions done by Moderator
    """
    def post(self, request):
        """
        This function handles the post request
        """
        if User.objects.filter(pk=self.request.user.id, groups__name="Moderator").exists():
            post_id = self.request.POST["post_id"]
            action = self.request.POST["action"]
            post = Post.objects.get(id=post_id)
            if action == "unpublish":
                post.is_published = False
                post.is_reported = False
                post.save()
                messages.info(request, "Post has been ubpublished")
            elif action == "delete":
                post.delete()
                messages.info(request, "Post has been deleted")
            elif action == "publish":
                post.is_published = True
                post.save()
                messages.info(request, "Post has been Published")
            else:
                pass
        return HttpResponseRedirect(reverse("dashboard"))
