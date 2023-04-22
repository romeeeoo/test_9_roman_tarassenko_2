from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import CreateView

from gallery.forms import PictureForm
from gallery.models import Picture


class AddNewPicture(LoginRequiredMixin, CreateView):
    template_name = "picture/add.html"
    model = Picture
    form_class = PictureForm

    def post(self, request, *args, **kwargs):
        form = self.get_form_class()(request.POST, request.FILES)
        if form.is_valid():
            author = request.user
            image = form.cleaned_data.get("image")
            description = form.cleaned_data.get("description")
            Picture.objects.create(image=image, author=author, description=description)
            return redirect("index")
        return redirect("index")
