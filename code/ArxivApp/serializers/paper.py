from rest_framework.serializers import ModelSerializer

from ArxivApp.models import Paper


class PaperSerializer(ModelSerializer):
    class Meta:
        model = Paper
        fields = [
            'id',
            'title',
            'authors',
            'summary',
            'comment',
            'subject_classification',
            'arxiv_id',
            'html_url',
            'pdf_url',
            'datetime_paper_published',
            'datetime_paper_updated'
        ]
        read_only_fields = [
            'id'
        ]
