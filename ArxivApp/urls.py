from django.urls import path
from rest_framework import routers
from ArxivApp.views import *

router = routers.SimpleRouter()

router.register(r'auth', AuthViewSet)

urlpatterns = []

urlpatterns += router.urls
