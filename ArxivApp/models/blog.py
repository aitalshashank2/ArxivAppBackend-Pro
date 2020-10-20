from ArxivApp.models.base import Model
from ArxivApp.models.user import User
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
    User,
    null=False,
    on_delete=models.CASCADE,
  )

  upvotes = models.PositiveIntegerField(
    default=0,
    null=False,
    blank=False,
  )

  downvotes = models.PositiveIntegerField(
    default=0,
    null=False,
    blank=False,
  )