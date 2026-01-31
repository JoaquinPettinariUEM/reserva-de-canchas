from rest_framework import serializers
from match_players.models import MatchPlayer
from core.serializers.match import MatchForPlayerSerializer
from matches.models import Match
from users.models import User

class MatchPlayerSerializer(serializers.ModelSerializer):
    match = MatchForPlayerSerializer(read_only=True)

    class Meta:
        model = MatchPlayer
        fields = ("id", "match")


class MatchPlayerCreateSerializer(serializers.ModelSerializer):
    match = serializers.PrimaryKeyRelatedField(
        queryset=Match.objects.all()
    )
    player = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=False
    )

    class Meta:
        model = MatchPlayer
        fields = ("match", "player")

    def validate(self, data): # type: ignore
        request = self.context["request"]

        if "player" in data and not request.user.is_superuser:
            raise serializers.ValidationError(
                "You cannot assign player manually"
            )

        return data

