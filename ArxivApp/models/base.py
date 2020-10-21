from django.db import models

class Model(models.Model):
  """
  This abstract root model should be inherited by all models
  It adds common features like date and time of creation and modification
  """

  datetime_created = models.DateTimeField(auto_now_add=True)
  datetime_modified = models.DateTimeField(auto_now=True)

  class Meta:
        
        abstract = True
