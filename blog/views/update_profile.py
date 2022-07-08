# pylint: disable=import-error, no-else-return

from django import views
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse
from django_email_verification import send_email
from blog.forms import ProfileUpdate
from blog.models import User


class UpdateProfile(LoginRequiredMixin, views.View):
    """
    This class will provide updation functionality to the user
    """
    model = User
    template_name = "registration/updateprofile.html"

    def get(self, request):
        """
        this method render the update form
        """
        user = request.user
        form = ProfileUpdate(request.POST or None, instance=user)
        context = {"form":form}
        return render(request, self.template_name, context)

    def post(self, request):
        """
        this method update the user data
        """
        user = self.request.user
        user_id = user.id
        mail = self.request.user.email
        new_mail = self.request.POST["email"]
        current_user = User.objects.get(id=user_id)
        current_user.first_name = self.request.POST["first_name"]
        current_user.last_name = self.request.POST["last_name"]
        if mail == new_mail:
            current_user.save()
            messages.success(request, "Profile has been successfully updated")
            return  HttpResponseRedirect(reverse("home"))
        else:
            current_user.email = self.request.POST["email"]
            current_user.is_active = False
            current_user.save()
            send_email(current_user)
            messages.warning(request, "You have changed Email,check your mail to confirm account")
            return HttpResponseRedirect(reverse("logout"))
