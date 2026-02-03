from rest_framework import viewsets, serializers
from django.core.exceptions import PermissionDenied
from .models import MatchPlayer
from .serializers import (
    MatchPlayerSerializer,
    MatchPlayerCreateSerializer
)
from core.permissions import IsPlayerOrAdmin


class MatchPlayerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsPlayerOrAdmin]
    queryset = MatchPlayer.objects.all()

    http_method_names = ["get", "post", "delete"]

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return MatchPlayer.objects.all()

        return MatchPlayer.objects.filter(player=user)

    def get_serializer_class(self):
        if self.action == "create":
            return MatchPlayerCreateSerializer
        return MatchPlayerSerializer

    def perform_create(self, serializer):
        user = self.request.user
        match = serializer.validated_data["match"]

        if match.match_players.count() >= match.court.capacity:
            raise serializers.ValidationError("Match is full")

        if (
            not user.is_superuser
            and MatchPlayer.objects.filter(
                match=match,
                player=user
            ).exists()
        ):
            raise serializers.ValidationError(
                "You are already registered in this match"
            )

        if user.is_superuser:
            serializer.save()
        else:
            serializer.save(player=user)

    def perform_destroy(self, instance):
        user = self.request.user

        if not user.is_superuser and instance.player != user:
            raise PermissionDenied(
                "You can only remove yourself from a match"
            )

        instance.delete()
