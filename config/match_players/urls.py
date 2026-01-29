from django.urls import path
from .views import MatchPlayerCreateDestroy

urlpatterns = [
    path("", MatchPlayerCreateDestroy.as_view()),
]
