from django.db import models
from django.contrib.auth.models import AbstractUser
from ArxivApp.models.paper import Paper

class User(AbstractUser):
  """
  This model contains information about the users of the app
  """

  username = models.CharField(
    max_length=15,
    blank=True,
    null=True,
    default=None,
    unique=True,
  )

  full_name = models.CharField(
    max_length=255
    blank=False,
    null=False    
  )

  email_address = models.EmailField(
    blank=False,
    null=False
  )

  bookmarks = models.ManyToManyField(
    'ArxivApp.Paper',
    null=True,
  )


