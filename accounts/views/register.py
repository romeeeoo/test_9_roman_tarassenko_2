import json

from django.contrib.auth import login
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from accounts.forms import CustomUserCreationForm
from accounts.views import SuccessUrlMixin


class RegisterView(View, SuccessUrlMixin):
    # template_name = "user_create.html"
    form_class = CustomUserCreationForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {"form": form}
        return render(request, "user_create.html", context)

    def post(self, request, *args, **kwargs):
        user_data = json.loads(request.body)
        form = self.form_class(user_data)
        if form.is_valid():
            user = form.save()
            login(request, user)
            success_url = self.get_success_url()
            return JsonResponse({"success_url": success_url})
        return JsonResponse({"error": "error"})
