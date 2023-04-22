from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from gallery.models import Picture


class DeletePicture(UserPassesTestMixin, DeleteView):
    template_name = "picture/confirm_delete.html"
    model = Picture
    success_url = reverse_lazy("index")

    def test_func(self):
        return self.get_object().author == self.request.user or self.request.user.has_perm("gallery.delete_picture")
