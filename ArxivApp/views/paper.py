from rest_framework import viewsets

from ArxivApp.models import Paper
from ArxivApp.serializers import PaperSerializer


class PaperViewSet(viewsets.ModelViewSet):

    queryset = Paper.objects.all()
    serializer_class = PaperSerializer
