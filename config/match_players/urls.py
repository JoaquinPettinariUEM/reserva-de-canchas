from django.urls import path
from .views import MatchPlayerCreate, MatchPlayerDelete, MatchPlayerDetail, MatchPlayerList

urlpatterns = [
    path("match/", MatchPlayerList.as_view(), name="match-player-list"),
    path("match/<int:pk>/", MatchPlayerDetail.as_view(), name="match-player-detail"),
    path("match/create/", MatchPlayerCreate.as_view(), name="match-player-create"),
    path("match/<int:pk>/delete/", MatchPlayerDelete.as_view(), name="match-player-delete"),
]
