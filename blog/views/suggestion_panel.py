# pylint: disable=no-member

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from blog.models import Suggestion


class SuggestionPanel(LoginRequiredMixin, TemplateView):
    """
    User dashboard will be handled through this class
    """
    template_name = "suggestion.html"
    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context['suggestions'] = Suggestion.objects.filter(
            suggestion_post__author=user).order_by('-time')
        context['posted_suggestions'] = Suggestion.objects.filter(
            suggestion_user=user).order_by('-time')
        replies = Suggestion.objects.filter(reply__suggestion_user=user)
        context['replies'] = replies
        return context
