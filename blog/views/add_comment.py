# pylint: disable=arguments-differ, no-else-return, no-member, too-many-ancestors

from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import redirect
from blog.models import Comment


class AddComment(CreateView):
    """
    this handles the functionality of adding comment
    """
    def post(self, request):
        post = self.request.POST["post_id"]
        comment = self.request.POST["comment"]
        parent_id = self.request.POST["parent_id"]
        user = self.request.user
        if comment:
            if parent_id == "":
                comment = Comment(comment_user=user, comment_content=comment, comment_post_id=post)
            else:
                parent = Comment.objects.get(id=parent_id)
                comment = Comment(
                    comment_user=user, comment_content=comment, comment_post_id=post, parent=parent)
            comment.save()
            messages.success(request, "Comment posted successfully")
            return redirect(f"/viewpost/{post}")
        else:
            messages.warning(request, "Comment can not be empty")
            return redirect(f"/viewpost/{post}")
