from typing import Any
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data: dict[str, Any] = super().validate(attrs)

        user = self.user
        assert user is not None

        data["user"] = {
            "id": getattr(user, "id", 0),
            "username": user.username,
            "email": user.email,
            "is_club_owner": getattr(user, "is_club_owner", False),
            "is_admin": user.is_superuser,
        }

        return data
