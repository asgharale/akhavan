from django.http import Http404
from rest_framework import status, generics, authentication, permissions
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView

from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer
from .filters import ArticleFilter
from .pagination import StandardPagination


class ArticleListView(generics.ListAPIView):
    permission_classes: list = [AllowAny]
    queryset = Article.published.all()
    filter_backends: list = [DjangoFilterBackend]
    serializer_class = ArticleListSerializer
    pagination_class = StandardPagination
    filterset_class = ArticleFilter

class ArticleDetailView(APIView):
    permission_classes: list = [AllowAny]

    def get_object(self, slug):
        try:
            return Article.published.get(address=slug)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, slug, fromat=None) -> Response:
        article = self.get_object(slug)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)