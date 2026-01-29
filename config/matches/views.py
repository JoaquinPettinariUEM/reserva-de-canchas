from rest_framework import generics
from django.core.exceptions import PermissionDenied
from .models import Match
from .serializers import MatchSerializer
from core.permissions import ReadOnlyOrClubAdmin

class MatchListCreate(generics.ListCreateAPIView):
    serializer_class = MatchSerializer
    permission_classes = [ReadOnlyOrClubAdmin]

    def get_queryset(self): # type: ignore
        user = self.request.user

        if user.is_authenticated and user.is_superuser:
            return Match.objects.all()

        if user.is_authenticated and getattr(user, "is_club_owner", False):
            return Match.objects.filter(court__owner=user)

        return Match.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        court = serializer.validated_data["court"]

        if user.is_superuser:
            serializer.save()
            return

        if court.owner != user:
            raise PermissionDenied("You do not own this match")

        serializer.save()

from rest_framework import generics
from rest_framework.exceptions import PermissionDenied
from .models import Match
from .serializers import MatchSerializer
from core.permissions import ReadOnlyOrClubAdmin

class MatchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Match.objects.select_related("court")
    serializer_class = MatchSerializer
    permission_classes = [ReadOnlyOrClubAdmin]

    def get_object(self):
        match = super().get_object()
        user = self.request.user

        if self.request.method in ("GET",) or user.is_authenticated and user.is_superuser:
            return match

        if getattr(user, "is_club_owner", False):
            if match.court.owner != user:
                raise PermissionDenied("You do not own this match")
            return match

        raise PermissionDenied("You cannot modify this match")

    def perform_update(self, serializer):
        if "court" in serializer.validated_data:
            raise PermissionDenied("Court cannot be changed")

        serializer.save()


