from django.urls import path

from gallery.views import PicturesView, AddNewPicture, PictureDetailView
from gallery.views.update_picture import UpdatePicture

urlpatterns = [
    path("", PicturesView.as_view(), name="index"),
    path("pictures/add/", AddNewPicture.as_view(), name="picture_add"),
    path("pictures/<int:pk>/", PictureDetailView.as_view(), name="detailed"),
    path("pictures/<int:pk>/update", UpdatePicture.as_view(), name="picture_update"),

]
