from rest_framework import serializers
from match_players.models import MatchPlayer

class MatchPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchPlayer
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
