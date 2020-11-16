from rest_framework import viewsets

from ArxivApp.models import User
from ArxivApp.serializers import UserGetSerializer, UserPostSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserPostSerializer
        return UserGetSerializer
