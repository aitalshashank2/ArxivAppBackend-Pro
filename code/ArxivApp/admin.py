from django.contrib import admin
from .models.paper import Paper
from .models.user import User
from .models.blog import Blog
from .models.download_location import DownloadLocation

# Register your models here.

admin.site.register(Paper)
admin.site.register(User)
admin.site.register(Blog)
admin.site.register(DownloadLocation)
