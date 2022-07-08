# pylint: disable=no-member
from django.contrib.auth.mixins import LoginRequiredMixin
from django import views
from django.http.response import Http404
from django.shortcuts import redirect
from blog.models import Likes, Post


class LikePost(LoginRequiredMixin, views.View):
    """
    This class handles the functionality of likes on posts
    """
    def post(self, request):
        """
        This function handles the post request
        """
        try:
            post_id = self.request.POST["post_id"]
            user = self.request.user
            if Likes.objects.filter(post_id=post_id, user=user).exists():
                Likes.objects.filter(user=user, post_id=post_id).delete()
            else:
                post = Post.objects.get(id=post_id)
                Likes.objects.create(user=user, post=post)
            return redirect(f"/viewpost/{post_id}")
        except:
            raise Http404
