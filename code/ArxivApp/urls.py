from django.urls import path
from rest_framework import routers
from ArxivApp.views import *

router = routers.SimpleRouter()

router.register(r'auth', AuthViewSet)
router.register(r'users', UserViewSet)
router.register(r'blogs', BlogViewSet)
router.register(r'papers', PaperViewSet)

urlpatterns = []

urlpatterns += router.urls
