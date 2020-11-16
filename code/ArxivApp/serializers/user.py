from rest_framework.serializers import ModelSerializer
from ArxivApp.models.user import User


class UserPostSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'full_name',
            'profile_picture',
            'email_address',
            'bookmarks',
        ]
        read_only_fields = ['id', ]


class UserGetSerializer(ModelSerializer):
    class Meta:
        model = User
        depth = 1
        fields = [
            'id',
            'username',
            'full_name',
            'profile_picture',
            'email_address',
            'bookmarks',
        ]
        read_only_fields = [
            'id',
            'username',
            'full_name',
            'profile_picture',
            'email_address',
            'bookmarks',
        ]
