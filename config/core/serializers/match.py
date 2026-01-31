from rest_framework import serializers
from matches.models import Match
from core.serializers.court import CourtMiniSerializer

# Lo tuve que mover por importación circular
class MatchForPlayerSerializer(serializers.ModelSerializer):
    court = CourtMiniSerializer(read_only=True)

    class Meta:
        model = Match
        fields = (
            "id",
            "court",
            "start_time",
            "end_time",
            "price",
        )
