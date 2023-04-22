from django.contrib.auth import get_user_model
from django.views.generic import DetailView


class UserDetailView(DetailView):
    model = get_user_model()
    template_name = "user_detail.html"
    context_object_name = "user_obj"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        favorite_pictures = self.object.favorite_pictures.all()
        context["pictures"] = favorite_pictures
        context["user_favorite"] = self.request.user.favorite_pictures.all()
        return context

