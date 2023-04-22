from django.views.generic import ListView

from gallery.models import Picture


class PicturesView(ListView):
    template_name = "picture/index.html"
    model = Picture
    context_object_name = "pictures"
    ordering = ("-created_at",)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["user_favorite"] = self.request.user.favorite_pictures.all()
        return context
