from rest_framework import serializers
from match_players.models import MatchPlayer
from core.serializers.match import MatchForPlayerSerializer

class MatchPlayerSerializer(serializers.ModelSerializer):
    match = MatchForPlayerSerializer(read_only=True)

    class Meta:
        model = MatchPlayer
        fields = (
            "id",
            "match",
        )
