from rest_framework import generics, serializers
from match_players.serializers import MatchPlayerSerializer

class MatchPlayerCreateDestroy(generics.CreateAPIView, generics.DestroyAPIView):
    serializer_class = MatchPlayerSerializer
    permission_classes = []

    def perform_create(self, serializer):
        match = serializer.validated_data["match"]

        if match.match_players.count() >= match.court.capacity:
            raise serializers.ValidationError("Match is full")

        serializer.save(player=self.request.user)
