from django.urls import path

from gallery.views import PicturesView, AddNewPicture, PictureDetailView

urlpatterns = [
    path("", PicturesView.as_view(), name="index"),
    path("pictures/add/", AddNewPicture.as_view(), name="picture_add"),
    path("pictures/<int:pk>/", PictureDetailView.as_view(), name="detailed"),

]
