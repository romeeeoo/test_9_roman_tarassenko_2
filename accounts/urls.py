from django.urls import path

from accounts.views import RegisterView, LoginView, UserDetailView, logout_view

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("accout/<int:pk>/", UserDetailView.as_view(), name="user_detailed")
]
