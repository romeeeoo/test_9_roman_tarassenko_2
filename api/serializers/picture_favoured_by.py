from rest_framework import serializers

from gallery.models import Picture


class PictureFavouredBySerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture.favored_by.through
        fields = ("id", "user_id", "picture_id")
        read_only_fields = ("id",)

