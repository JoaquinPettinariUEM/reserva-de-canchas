from django.core.management.base import BaseCommand
from core.seeds.seed_users import seed_users
from core.seeds.seed_courts import seed_courts
from core.seeds.seed_matches import seed_matches
from core.seeds.seed_match_players import seed_match_players


class Command(BaseCommand):
    help = "Seed initial data"

    def handle(self, *args, **kwargs):
        self.stdout.write("🌱 Seeding users...")
        seed_users(self.stdout)

        self.stdout.write("🌱 Seeding courts...")
        seed_courts(self.stdout)

        self.stdout.write("🌱 Seeding matches...")
        seed_matches(self.stdout)

        self.stdout.write("🌱 Seeding match players...")
        seed_match_players(self.stdout)

        self.stdout.write(self.style.SUCCESS("✅ Seeding completed"))
