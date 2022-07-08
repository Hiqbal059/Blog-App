# pylint: disable=no-else-return, no-member

from django.contrib.auth.mixins import LoginRequiredMixin
from django import views
from django.contrib import messages
from django.shortcuts import redirect
from blog.models import Post, Comment


class Report(LoginRequiredMixin, views.View):
    """
    This class handles the functionality of Report the Posts and Comment
    """
    def post(self, request):
        """
        This function handles the post request
        """
        post_id = self.request.POST["post_id"]
        comment_id = self.request.POST["comment_id"]
        print(comment_id)
        if comment_id == '0':
            post = Post.objects.get(id=post_id)
            post.is_reported = True
            post.save()
            messages.warning(request, "Post has been reported, Moderator will take action soon")
            return redirect("home")
        else:
            comment = Comment.objects.get(id=comment_id)
            comment.is_reported = True
            comment.save()
            messages.warning(request, "Comment has been reported")
            return redirect(f"/viewpost/{post_id}")
