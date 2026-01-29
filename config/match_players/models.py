from django.db import models
from matches.models import Match
from users.models import User

class MatchPlayer(models.Model):
  match = models.ForeignKey(
    Match,
    on_delete=models.CASCADE,
    related_name="match_players"
  )

  player = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name="player_on_match"
  )

  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
      return f"{self.match} - {self.player}"
