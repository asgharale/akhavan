from django.urls import path
from .views import ArticleListView


urlpatterns = [
    path("v1/list", ArticleListView.as_view()),
    # path("v1/<slug:address>", ArticleDetailView.as_view()),
    # path("v1/<pk:id>", ArticleDetailView)
]
