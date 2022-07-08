# pylint: disable=missing-module-docstring, import-error, too-many-ancestors
from django.contrib.messages.views import SuccessMessageMixin
from django.urls.base import reverse_lazy
from django.views.generic import CreateView
from blog.forms import SignupForm
from django_email_verification import send_email

class UserRegister(SuccessMessageMixin, CreateView):
    """
    This class will register the user
    """
    form_class = SignupForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")
    success_message = "Account successful created check your mail for activation"

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        returnval = super(UserRegister, self).form_valid(form)
        send_email(user)
        return returnval
