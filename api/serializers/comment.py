from rest_framework import serializers

from api.serializers import AuthorSerializer
from gallery.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    datetime_created = serializers.DateTimeField(format='%B %-d, %Y, %-I:%M %p')

    class Meta:
        model = Comment
        fields = ("id", "text", "picture", "author", "datetime_created")
        read_only_fields = ("id",)


class CommentSerializerGet(CommentSerializer):
    author = AuthorSerializer(read_only=True)