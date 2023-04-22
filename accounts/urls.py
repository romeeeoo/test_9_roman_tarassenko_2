from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from accounts.views import RegisterView, LoginView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("api-login/", obtain_auth_token, name='api_token_auth'),
]
