import requests
import feedparser

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated

from ArxivApp.models import Paper
from ArxivApp.constants import subject_classifications
from ArxivApp.serializers import PaperSerializer


class PaperViewSet(viewsets.ModelViewSet):

    queryset = Paper.objects.all()
    serializer_class = PaperSerializer
    permission_classes = (IsAuthenticated,)

    @action(detail=False, methods=['get', ],)
    def search(self, request, *args, **kwargs):
        """
        Sends POST request to arxiv api and retrieves results matching the query parameters
        """

        search_params = request.query_params

        title = search_params.get('ti', None)
        author = search_params.get('au', None)
        abstract = search_params.get('abs', None)
        comment = search_params.get('co', None)
        journal_reference = search_params.get('jr', None)
        category = search_params.get('cat', None)

        url_params = ""

        for key, value in search_params.items():
            if url_params != "":
                url_params += "+AND+"
            value = value.replace(' ', '_').lower()
            url_params += f'{key}:{value}'

        url_params += "&start=0&max_results=5"
        arxiv_url = f'http://export.arxiv.org/api/query?search_query={url_params}'

        arxiv_response = requests.get(arxiv_url)
        feed = feedparser.parse(arxiv_response.text)

        entries = feed.entries
        feed = feed.feed

        if feed.opensearch_totalresults == 1 and entries[0].title == "Error":
            return Response({'Error': entries[0].summary, }, status=status.HTTP_400_BAD_REQUEST)

        papers = {
            'arxiv_id': [],
            'published_time': [],
            'update_time': [],
            'title': [],
            'summary': [],
            'authors': [],
            'comments': [],
            'journal_references': [],
            'category': [],
            'pdf_url': [],
            'html_url': [],
        }
        keys = list(papers.keys())

        for entry in entries:

            try:
                arxiv_id = entry.id.split('/abs/')[-1]
            except Exception:
                arxiv_id = ""

            try:
                published = entry.published
            except Exception:
                published = ""

            try:
                updated = entry.updated
            except Exception:
                updated = ""

            try:
                title = entry.title
            except Exception:
                title = ""

            try:
                summary = entry.summary
            except Exception:
                summary = ""

            try:
                authors = '&#&'.join(author.name for author in entry.authors)
            except Exception:
                authors = ""

            html_url = ""
            pdf_url = ""
            try:
                for link in entry.links:
                    if link.rel == 'alternate':
                        html_url = link.href
                    elif link.title == 'pdf':
                        pdf_url = link.href
            except:
                pass

            try:
                journal_ref = entry.arxiv_journal_ref
            except Exception:
                journal_ref = ""

            try:
                comment = entry.arxiv_comment
            except Exception:
                comment = ""

            try:
                categories = '|'.join(tag['term'] for tag in entry.tags)
            except Exception:
                categories = ""

            papers[keys[0]].append(arxiv_id)
            papers[keys[1]].append(published)
            papers[keys[2]].append(updated)
            papers[keys[3]].append(title)
            papers[keys[4]].append(summary)
            papers[keys[5]].append(authors)
            papers[keys[6]].append(comment)
            papers[keys[7]].append(journal_ref)
            papers[keys[8]].append(categories)
            papers[keys[9]].append(html_url)
            papers[keys[10]].append(pdf_url)

        return Response({'Results': papers}, status=status.HTTP_200_OK)
