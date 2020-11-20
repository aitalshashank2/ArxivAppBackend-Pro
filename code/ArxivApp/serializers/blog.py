from rest_framework.serializers import ModelSerializer

from ArxivApp.serializers import UserPostSerializer
from ArxivApp.models import Blog


class BlogSerializer(ModelSerializer):
    # author = UserPostSerializer()
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
