from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from api.views import FavouriteApiView, CommentViewSet


router = routers.DefaultRouter()
router.register(r"comments", CommentViewSet, "comment")

urlpatterns = [
    path("toggle-favourite/", FavouriteApiView.as_view(), name="toggle_favorite"),
    path("", include(router.urls)),
    path("login/", obtain_auth_token, name='api_token_auth'),

]
