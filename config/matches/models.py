from django.db import models
from courts.models import Court

class Match(models.Model):

    court = models.ForeignKey(
        Court,
        on_delete=models.CASCADE,
        related_name="matches"
    )

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    max_players = models.PositiveIntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["court", "start_time"],
                name="unique_match_per_court_and_start_time"
            )
        ]
        ordering = ["start_time"]
        indexes = [
            models.Index(fields=["court", "start_time", "end_time"])
        ]

    def __str__(self):
        return f"{self.court} | {self.start_time}"
