from django.urls import path

from gallery.views import PicturesView, AddNewPicture

urlpatterns = [
    path("", PicturesView.as_view(), name="index"),
    path("pictures/add/", AddNewPicture.as_view(), name="picture_add"),
]
