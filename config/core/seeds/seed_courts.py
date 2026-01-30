from courts.models import Court
from django.contrib.auth import get_user_model
from decimal import Decimal

User = get_user_model()


def seed_courts(stdout=None):
    owners = User.objects.filter(is_club_owner=True)

    courts_data = [
        # OWNER 1
        {
            "sport": Court.Sport.FOOTBALL,
            "location": "Cancha Central",
            "capacity": 10,
            "price_per_hour": Decimal("80.00"),
            "match_duration": Court.MatchDuration.MIN_90,
        },
        {
            "sport": Court.Sport.TENNIS,
            "location": "Cancha Tenis Norte",
            "capacity": 2,
            "price_per_hour": Decimal("30.00"),
            "match_duration": Court.MatchDuration.MIN_60,
        },

        # OWNER 2
        {
            "sport": Court.Sport.PADDLE,
            "location": "Paddle Club Indoor",
            "capacity": 4,
            "price_per_hour": Decimal("40.00"),
            "match_duration": Court.MatchDuration.MIN_90,
        },
        {
            "sport": Court.Sport.FOOTBALL,
            "location": "Fútbol 5 Sur",
            "capacity": 10,
            "price_per_hour": Decimal("70.00"),
            "match_duration": Court.MatchDuration.MIN_60,
        },
    ]

    created = 0

    for owner, court_data in zip(owners, courts_data):
        court, exists = Court.objects.get_or_create(
            owner=owner,
            location=court_data["location"],
            defaults=court_data,
        )

        if exists:
            created += 1
            if stdout:
                stdout.write(f"✅ Court created: {court}")
        else:
            if stdout:
                stdout.write(f"⚠️ Court already exists: {court}")

    return created
