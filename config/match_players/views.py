from rest_framework import generics, serializers
from django.core.exceptions import PermissionDenied
from .models import MatchPlayer
from .serializers import MatchPlayerSerializer, MatchPlayerCreateSerializer
from core.permissions import IsPlayerOrAdmin

class MatchPlayerList(generics.ListAPIView):
    serializer_class = MatchPlayerSerializer
    permission_classes = [IsPlayerOrAdmin]

    def get_queryset(self): # type: ignore
        user = self.request.user

        if user.is_authenticated and user.is_superuser:
            return MatchPlayer.objects.all()

        return MatchPlayer.objects.filter(player=user)

class MatchPlayerDetail(generics.RetrieveAPIView):
    queryset = MatchPlayer.objects.all()
    serializer_class = MatchPlayerSerializer
    permission_classes = [IsPlayerOrAdmin]

class MatchPlayerCreate(generics.CreateAPIView):
    permission_classes = [IsPlayerOrAdmin]

    def get_serializer_class(self): # type: ignore
        if self.request.method == "POST":
            return MatchPlayerCreateSerializer
        return MatchPlayerSerializer

    def perform_create(self, serializer):
        user = self.request.user
        match = serializer.validated_data["match"]

        if match.match_players.count() >= match.court.capacity:
            raise serializers.ValidationError("Match is full")

        if not user.is_superuser and MatchPlayer.objects.filter(
                match=match,
                player=user
            ).exists():
                raise serializers.ValidationError(
                    "You are already registered in this match"
                )

        if user.is_superuser:
            serializer.save()
        else:
            serializer.save(player=user)


class MatchPlayerDelete(generics.DestroyAPIView):
    queryset = MatchPlayer.objects.all()
    serializer_class = MatchPlayerSerializer
    permission_classes = [IsPlayerOrAdmin]

    def perform_destroy(self, instance):
        user = self.request.user

        if not user.is_superuser and instance.player != user:
            raise PermissionDenied("You can only remove yourself from a match")

        instance.delete()
