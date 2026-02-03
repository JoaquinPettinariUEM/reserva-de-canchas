from matches.models import Match
from courts.models import Court
from django.utils import timezone
from decimal import Decimal
from datetime import datetime, timedelta, time


def seed_matches(stdout=None):
    courts = Court.objects.all()

    base_date = timezone.localdate()
    fixed_hour = time(18, 0)  # 18:00 exacto

    created = 0

    for i, court in enumerate(courts):
        start_time = timezone.make_aware(
            datetime.combine(
                base_date + timedelta(days=i + 1),
                fixed_hour
            )
        )

        duration = timedelta(minutes=court.match_duration)

        match, created_flag = Match.objects.get_or_create(
            court=court,
            start_time=start_time,
            defaults={
                "end_time": start_time + duration,
                "price": Decimal(court.price_per_hour),
                "max_players": court.capacity,
            },
        )


        if created_flag:
            created += 1
            if stdout:
                stdout.write(f"✅ Match created: {match}")
        else:
            if stdout:
                stdout.write(f"⚠️ Match already exists: {match}")

    return created
