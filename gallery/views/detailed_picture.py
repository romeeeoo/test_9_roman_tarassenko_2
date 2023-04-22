from django.views.generic import DetailView

from gallery.models import Picture


class PictureDetailView(DetailView):
    template_name = "picture/detailed.html"
    model = Picture

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        picture = self.object
        picture_favoured_by = picture.favored_by.all()
        context["picture_favoured_by"] = picture_favoured_by
        if self.request.user.is_authenticated:
            context["user_favorite"] = self.request.user.favorite_pictures.all()
        return context
