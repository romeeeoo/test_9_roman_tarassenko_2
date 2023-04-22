import json

from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.generic import TemplateView

from accounts.forms import LoginForm
from accounts.views import SuccessUrlMixin


class LoginView(TemplateView, SuccessUrlMixin):
    template_name = "login.html"
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {"form": form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        user_data = json.loads(request.body)
        form = self.form_class(user_data)
        if not form.is_valid():
            return self.render_to_response(form)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if not user:
            return JsonResponse({"error": "incorrect password or username"})
        login(request, user)
        success_url = self.get_success_url()
        return JsonResponse({"success_url": success_url})
