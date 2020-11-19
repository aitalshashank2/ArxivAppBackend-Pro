import json
import requests
import feedparser
import dateutil.parser

from rest_framework.viewsets import ModelViewSet
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_409_CONFLICT
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated

from ArxivAppBackend.settings import CONFIG_VARS

from ArxivApp.models.user import User
from ArxivApp.models.paper import Paper
from ArxivApp.models.download_location import DownloadLocation
from ArxivApp.serializers.user import UserGetSerializer, UserPostSerializer


class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == "create" or self.action == "update" or self.action == "partial":
            return UserPostSerializer
        else:
            return UserGetSerializer

    @action(detail=False, methods=['post', ],)
    def bookmark(self, request, *args, **kwargs):
        data = request.data
        
        action = data.get('action', None)
        arxiv_id = data.get('arxiv_id', None)

        if action is None:
            return Response({'Error': 'Action not provided'}, status=HTTP_400_BAD_REQUEST)
        
        if arxiv_id is None:
            return Response({'Error': 'Paper id not provided'}, status=HTTP_400_BAD_REQUEST)
        
        user = request.user

        if action == "add":
            try:
                papers = user.bookmarks.filter(arxiv_id=arxiv_id)
                if len(papers) == 1:
                    return Response({'Error': 'Paper already bookmarked'}, status=HTTP_409_CONFLICT)  
                elif len(papers) > 1:
                    for paper in papers:
                        user.bookmarks.remove(paper)
            except Exception as e:  
                return Response({'Error': str(e)}) 
            
            try:
                paper = Paper.objects.get(arxiv_id=arxiv_id)
            except Paper.DoesNotExist:
                arxiv_url = f'http://export.arxiv.org/api/query?id_list={arxiv_id}'
                response = requests.get(arxiv_url)
                feed = feedparser.parse(response.text)

                entries = feed.entries
                feed = feed.feed

                if feed.opensearch_totalresults == 1 and entries[0].title == "Error":
                    return Response({'Error': 'Invalid arxiv_id', }, status=status.HTTP_400_BAD_REQUEST)
                
                entry = entries[0]

                try:
                    arxiv_id = entry.id.split('/abs/')[-1]
                except Exception:
                    arxiv_id = ""

                try:
                    published = entry.published
                    published = dateutil.parser.parse(published)
                except Exception as e:
                    return Response({'Error': f'Paper does not have publish date, not authentic: {str(e)}'}, status=HTTP_400_BAD_REQUEST)

                try:
                    updated = entry.updated
                    updated = dateutil.parser.parse(updated)
                except Exception as e:
                    return Response({'Error': f'Paper does not have update date, not authentic: {str(e)}'}, status=HTTP_400_BAD_REQUEST)

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
                    comment = entry.arxiv_comment
                except Exception:
                    comment = ""

                try:
                    categories = '|'.join(tag['term'] for tag in entry.tags)
                except Exception:
                    categories = ""
                
                paper = Paper(
                    arxiv_id=arxiv_id,
                    datetime_paper_published=published,
                    datetime_paper_updated=updated,
                    title=title,
                    summary=summary,
                    authors=authors,
                    comment=comment,
                    subject_classification=categories,
                    html_url=html_url,
                    pdf_url=pdf_url,
                )

                paper.save()

            user.bookmarks.add(paper)
            user.save()

            return Response({'Status': 'Bookmark created successfully'}, status=HTTP_200_OK)

        elif action == "remove":
            try:
                papers = user.bookmarks.all()
                papers = papers.filter(arxiv_id=arxiv_id)
                if len(papers) == 0:
                    return Response({'Error': 'Bookmark with provided id does not exist'}, status=HTTP_409_CONFLICT)  
                else:
                    for paper in papers:
                        user.bookmarks.remove(paper)
                    user.save()
                    return Response({'Status': 'Bookmark removed successfully'}, status=HTTP_200_OK)

            except Exception as e:  
                return Response({'Error': str(e)}) 
        else:
            return Response({'Error': 'Incorrect action provided'}, status=HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post', ],)
    def download(self, request, *args, **kwargs):
        data = request.data
        
        action = data.get('action', None)
        arxiv_id = data.get('arxiv_id', None)

        if action is None:
            return Response({'Error': 'Action not provided'}, status=HTTP_400_BAD_REQUEST)
        
        if arxiv_id is None:
            return Response({'Error': 'Paper id not provided'}, status=HTTP_400_BAD_REQUEST)
        
        user = request.user

        if action == "add":
            try:
                papers = user.downloads.filter(arxiv_id=arxiv_id)
                if len(papers) == 1:
                    return Response({'Error': 'Paper already downloaded'}, status=HTTP_409_CONFLICT)  
                elif len(papers) > 1:
                    for paper in papers:
                        user.downloads.remove(paper)
            except Exception as e:  
                return Response({'Error': str(e)}) 
            
            try:
                paper = Paper.objects.get(arxiv_id=arxiv_id)
            except Paper.DoesNotExist:
                arxiv_url = f'http://export.arxiv.org/api/query?id_list={arxiv_id}'
                response = requests.get(arxiv_url)
                feed = feedparser.parse(response.text)

                entries = feed.entries
                feed = feed.feed

                if feed.opensearch_totalresults == 1 and entries[0].title == "Error":
                    return Response({'Error': 'Invalid arxiv_id', }, status=status.HTTP_400_BAD_REQUEST)
                
                entry = entries[0]

                try:
                    arxiv_id = entry.id.split('/abs/')[-1]
                except Exception:
                    arxiv_id = ""

                try:
                    published = entry.published
                    published = dateutil.parser.parse(published)
                except Exception as e:
                    return Response({'Error': f'Paper does not have publish date, not authentic: {str(e)}'}, status=HTTP_400_BAD_REQUEST)

                try:
                    updated = entry.updated
                    updated = dateutil.parser.parse(updated)
                except Exception as e:
                    return Response({'Error': f'Paper does not have update date, not authentic: {str(e)}'}, status=HTTP_400_BAD_REQUEST)

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
                    comment = entry.arxiv_comment
                except Exception:
                    comment = ""

                try:
                    categories = '|'.join(tag['term'] for tag in entry.tags)
                except Exception:
                    categories = ""
                
                paper = Paper(
                    arxiv_id=arxiv_id,
                    datetime_paper_published=published,
                    datetime_paper_updated=updated,
                    title=title,
                    summary=summary,
                    authors=authors,
                    comment=comment,
                    subject_classification=categories,
                    html_url=html_url,
                    pdf_url=pdf_url,
                )

                paper.save()
            

            download_url = data.get('download_url', None)
            if download_url is None:
                return Response({'Error': 'Download Url Not Provided.'}, status=HTTP_400_BAD_REQUEST)

            download = DownloadLocation.objects.create(
                user=user,
                paper=paper,
                html_url=download_url,
            )
            download.save()

            return Response({'Status': 'Download created successfully'}, status=HTTP_200_OK)

        elif action == "remove":
            try:
                papers = user.downloads.all()
                if len(papers) == 0:
                    return Response({'Error': 'Download with provided id does not exist'}, status=HTTP_409_CONFLICT)  
                else:
                    for paper in papers:
                        download = DownloadLocation.objects.get(user=user, paper=paper)
                        download.delete()

                    return Response({'Status': 'Download removed successfully'}, status=HTTP_200_OK)

            except Exception as e:  
                return Response({'Error': str(e)}) 
        else:
            return Response({'Error': 'Incorrect action provided'}, status=HTTP_400_BAD_REQUEST)
