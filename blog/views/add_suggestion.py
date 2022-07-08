# pylint: disable= no-member

from django import views
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from blog.models import Post, Suggestion


class AddSuggestion(LoginRequiredMixin, views.View):
    """
    this handles the functionality of adding Suggestion
    """
    def post(self, request):
        """
        This function handles the post request
        """
        post_id = self.request.POST["post_id"]
        suggestion = self.request.POST["suggestion"]
        user = request.user
        if suggestion:
            post = Post.objects.get(id=post_id)
            Suggestion.objects.create(
                suggestion_user=user, suggestion_content=suggestion, suggestion_post=post)
            messages.warning(request, "Suggestion has been submitted to Author")
        else:
            messages.warning(request, "Suggestion cannot be empty")
        return redirect(f"/viewpost/{post_id}")
