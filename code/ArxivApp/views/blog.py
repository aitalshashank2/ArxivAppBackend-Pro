from rest_framework import viewsets

from ArxivApp.models import Blog
from ArxivApp.serializers import BlogSerializer


class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
