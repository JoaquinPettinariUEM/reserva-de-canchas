from matches.models import Match
from match_players.models import MatchPlayer
from django.contrib.auth import get_user_model

User = get_user_model()


def seed_match_players(stdout=None):
    players = list(
        User.objects.filter(is_club_owner=False, is_staff=False)
    )
    matches = Match.objects.all()

    created = 0
    player_index = 0
    for match in matches:
        max_players = match.max_players or 0

        for _ in range(max_players // 2):
            if player_index >= len(players):
                break

            player = players[player_index]
            player_index += 1

            _, exists = MatchPlayer.objects.get_or_create(
                match=match,
                player=player,
            )

            if exists:
                created += 1
                if stdout:
                    stdout.write(
                        f"✅ Player {player.username} added to match {getattr(match, 'id', 0)}"
                    )

    return created
