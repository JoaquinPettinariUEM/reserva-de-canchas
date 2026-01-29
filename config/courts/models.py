from django.db import models
from django.conf import settings


class Court(models.Model):

    class Sport(models.TextChoices):
        FOOTBALL = "football", "Football"
        TENNIS = "tennis", "Tennis"
        PADDLE = "paddle", "Paddle"

    class MatchDuration(models.IntegerChoices):
        MIN_60 = 60, "60 minutes"
        MIN_90 = 90, "90 minutes"
        MIN_120 = 120, "120 minutes"

    sport = models.CharField(
        max_length=20,
        choices=Sport.choices
    )
    location = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    price_per_hour = models.DecimalField(max_digits=8, decimal_places=2)
    match_duration = models.IntegerField(choices=MatchDuration.choices)

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="courts"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sport} - {self.location}"
