from rest_framework import serializers
from matches.models import Match
from core.serializers.court import CourtMiniSerializer
from courts.models import Court
from django.utils import timezone

class MatchForCourtSerializer(serializers.ModelSerializer):
    is_full = serializers.SerializerMethodField()
    is_in = serializers.SerializerMethodField()
    court = CourtMiniSerializer()

    class Meta:
        model = Match
        fields = (
            "id",
            "court",
            "start_time",
            "end_time",
            "price",
            "is_full",
            "is_in"
        )

    def get_is_full(self, obj):
        if obj.max_players is None:
            return False

        return obj.match_players.count() >= obj.max_players

    def get_is_in(self, obj):
        request = self.context.get("request")

        if not request or not request.user.is_authenticated:
            return False

        return obj.match_players.filter(
            player=request.user
        ).exists()

class MatchCreateSerializer(serializers.ModelSerializer):
    court = serializers.PrimaryKeyRelatedField(
        queryset=Court.objects.all()
    )

    def validate(self, data):
        start = data.get("start_time")
        end = data.get("end_time")

        if start >= end:
            raise serializers.ValidationError(
                "end_time must be after start_time"
            )

        if start <= timezone.now():
            raise serializers.ValidationError(
                "start_time must be in the future"
            )

        return data

    class Meta:
        model = Match
        fields = (
            "court",
            "start_time",
            "end_time",
            "price",
            "max_players",
        )
