# pylint: disable=arguments-differ, no-member, too-many-ancestors
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.shortcuts import redirect
from blog.models import Likes, Comment


class LikeComment(LoginRequiredMixin, UpdateView):
    """
    This function handles the functionality of likes the comments
    """
    def post(self, request):
        """
        This function handles the post request
        """
        post = self.request.POST["post_id"]
        comment_id = self.request.POST["comment_id"]
        user = self.request.user
        like = Likes.objects.filter(comment_id=comment_id, user=user)
        if like.exists():
            like.delete()
        else:
            comment = Comment.objects.get(id=comment_id, comment_user=user)
            Likes.objects.create(user=user, comment=comment)
        return redirect(f"/viewpost/{post}")
