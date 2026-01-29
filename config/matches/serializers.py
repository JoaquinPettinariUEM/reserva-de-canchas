from rest_framework import serializers
from datetime import timedelta
from .models import Match

from rest_framework import serializers
from .models import Match

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = "__all__"
        read_only_fields = ["id", "created_at", ]
