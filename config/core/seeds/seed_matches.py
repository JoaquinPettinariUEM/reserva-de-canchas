from matches.models import Match
from courts.models import Court
from django.utils import timezone
from datetime import timedelta
from decimal import Decimal


def seed_matches(stdout=None):
    courts = Court.objects.all()
    now = timezone.now()

    created = 0

    for i, court in enumerate(courts):
        start_time = now + timedelta(days=i + 1, hours=18)
        duration = timedelta(minutes=court.match_duration)

        match, exists = Match.objects.get_or_create(
            court=court,
            start_time=start_time,
            end_time=start_time + duration,
            defaults={
                "price": Decimal(court.price_per_hour),
                "max_players": court.capacity,
            },
        )

        if exists:
            created += 1
            if stdout:
                stdout.write(f"✅ Match created: {match}")
        else:
            if stdout:
                stdout.write(f"⚠️ Match already exists: {match}")

    return created
