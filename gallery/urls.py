from django.urls import path

from gallery.views import PicturesView

urlpatterns = [
    path("", PicturesView.as_view(), name="index"),
]
