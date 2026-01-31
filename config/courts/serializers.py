from rest_framework import serializers
from courts.models import Court
from matches.serializers import MatchForCourtSerializer


class CourtSerializer(serializers.ModelSerializer):
    matches = MatchForCourtSerializer(many=True, read_only=True)

    class Meta:
        model = Court
        fields = (
            "id",
            "owner",
            "name",
            "sport",
            "location",
            "capacity",
            "price_per_hour",
            "match_duration",
            "created_at",
            "matches",
        )

class CourtCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Court
        fields = (
            "name",
            "location",
            "capacity",
            "price_per_hour",
            "match_duration",
            "sport",
        )
