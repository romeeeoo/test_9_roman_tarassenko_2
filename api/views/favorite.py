from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from gallery.models import Picture


class FavouriteApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = request.data
        picture_id = data.get("picture_id")
        picture = Picture.objects.get(pk=picture_id)
        if request.user.favorite_pictures.filter(pk=picture_id):
            request.user.favorite_pictures.remove(picture)
            print("picture removed from favourite")
            data = {"button_status": "like"}
            return Response(data=data, status=203)
        else:
            request.user.favorite_pictures.add(picture)
            print("picture added to favourite")
            data = {"button_status": "dislike"}
            return Response(data=data, status=201)
