# pylint: disable=no-member

from django.contrib.auth.mixins import LoginRequiredMixin
from django import views
from django.shortcuts import redirect
from blog.models import Suggestion


class SuggestionAction(LoginRequiredMixin, views.View):
    """
    This class handles the functionality of action on suggestions by author
    """
    def post(self, request):
        """
        This function handles the post request
        """
        suggestion_id = self.request.POST["suggestion_id"]
        status = self.request.POST["status"]
        suggestion_post = Suggestion.objects.get(id=suggestion_id)
        if request.user == suggestion_post.suggestion_post.author:
            if status == "modified":
                suggestion_post.status = "modified"
            elif status == "rejected":
                suggestion_post.status = "rejected"
            elif status == "replied":
                suggestion_post.status = "replied"
                reply_content = self.request.POST["reply_suggestion"]
                parent = Suggestion.objects.get(id=suggestion_id)
                Suggestion.objects.create(
                    reply=parent, suggestion_user=request.user,
                    suggestion_content=reply_content, suggestion_post=parent.suggestion_post)
            else:
                suggestion_post.status = "suggested"
        suggestion_post.save()
        return redirect(f"/suggestion/{suggestion_id}")
