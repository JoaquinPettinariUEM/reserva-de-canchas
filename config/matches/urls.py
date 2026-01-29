from django.urls import path
from .views import MatchListCreate, MatchDetail

urlpatterns = [
    path(
        "",
        MatchListCreate.as_view(),
        name="match-list-create"
    ),
    path(
        "<int:pk>/",
        MatchDetail.as_view(),
        name="match-detail"
    ),
]

