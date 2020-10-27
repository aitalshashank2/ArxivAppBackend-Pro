from django.db import models
from django.contrib.auth.models import AbstractUser
from ArxivApp.constants import defaults

class User(AbstractUser):
  """
  This model contains information about the users of the app
  """

  username = models.CharField(
    max_length=31,
    blank=True,
    null=True,
    default=None,
    unique=True,
  )

  full_name = models.CharField(
    max_length=255,
    blank=False,
    null=False    
  )

  profile_picture = models.TextField(
    blank=False,
    null=False,
    default=defaults.PROFILE_PICTURE,
  )

  email_address = models.EmailField(
    blank=False,
    null=False,
  )

  bookmarks = models.ManyToManyField(
    'ArxivApp.Paper',
    related_name='bookmark_users',
    blank=True,
  )

  downloads = models.ManyToManyField(
    'ArxivApp.Paper',
    related_name='download_users',
    through='ArxivApp.DownloadLocation',
    blank=True,
  )

  def __str__(self):

    return self.full_name
