from django.contrib.auth import get_user_model
from django.db import models


class Comment(models.Model):
    class Meta:
        ordering = ("-datetime_created",)

    text = models.TextField(
        blank=False,
        null=False,
        max_length=200
    )
    picture = models.ForeignKey(
        to="Picture",
        related_name="comments",
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        to=get_user_model(),
        related_name="comments",
        null=False, blank=False,
        on_delete=models.CASCADE
    )
    datetime_created = models.DateTimeField(
        auto_now_add=True
    )
