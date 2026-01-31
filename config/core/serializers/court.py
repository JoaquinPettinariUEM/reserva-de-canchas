from rest_framework import serializers
from courts.models import Court

# Lo tuve que mover por importación circular
class CourtMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Court
        fields = (
            "id",
            "sport",
            "location",
            "name"
        )
