from ArxivApp.models.base import Model
from django.conf import settings
from django.db import models


class Blog(Model):
    """
    This models hold information about the blog posts that are
    posted by users of ArxivApp
    """

    title = models.CharField(
        max_length=127,
    )

    body = models.TextField()

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=False,
        on_delete=models.CASCADE,
    )

    votes = models.IntegerField(
        default=0,
        null=False,
        blank=False,
    )

    def __str__(self):

        return f'{self.title} - by - {self.author.full_name}'
