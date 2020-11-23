from rest_framework.serializers import ModelSerializer
from ArxivApp.models import Blog


class BlogPostSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            'id',
            'title',
            'body',
            'author',
            'votes',
        ]
        read_only_fields = [
            'id',
            'author',
            'votes',
        ]

class BlogGetSerializer(ModelSerializer):
    class Meta:
        model = Blog
        depth = 1
        fields = [
            'id',
            'title',
            'body',
            'author',
            'votes',
        ]
        read_only_fields = [
            'id',
            'title',
            'body',
            'author',
            'votes',
        ]
