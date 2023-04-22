import datetime
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.permissions import DeleteCommentPermission
from api.serializers import CommentSerializer
from api.serializers.comment import CommentSerializerGet
from gallery.models import Comment


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, DeleteCommentPermission]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request,  *args, **kwargs):
        data = request.data
        print(data)
        request_data = {
                "text": data.get("text"),
                "picture": data.get("picture_id"),
                "author": request.user.pk,
                "datetime_created": datetime.datetime.now()
        }
        serializer = self.get_serializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        response_serializer = CommentSerializerGet(serializer.instance)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    