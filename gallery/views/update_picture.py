from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse
from django.views.generic import UpdateView

from gallery.forms import PictureForm
from gallery.models import Picture


class UpdatePicture(UserPassesTestMixin, UpdateView):
    form_class = PictureForm
    model = Picture
    template_name = "picture/update.html"

    def get_success_url(self):
        return reverse("detailed", kwargs={"pk": self.object.pk})

    def test_func(self):
        return self.get_object().author == self.request.user or self.request.user.has_perm("gallery.change_picture")
