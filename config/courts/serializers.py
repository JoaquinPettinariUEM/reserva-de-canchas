from rest_framework import serializers
from .models import Court
from users.models import User

class CourtSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(is_club_owner=True),
        required=False
    )

    class Meta:
        model = Court
        fields = "__all__"
        read_only_fields = ["id"]
