from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


USERS = [
    # ADMINS
    {
        "email": "admin1@gmail.com",
        "username": "admin1",
        "document": "admin1",
        "password": "admin123",
        "is_superuser": True,
        "is_staff": True,
    },

    # CLUB OWNERS
    {
        "email": "club1@gmail.com",
        "username": "club1",
        "document": "club1",
        "password": "club123",
        "is_club_owner": True,
    },
    {
        "email": "club2@gmail.com",
        "username": "club2",
        "document": "club2",
        "password": "club123",
        "is_club_owner": True,
    },

    # PLAYERS
    {
        "email": "player1@gmail.com",
        "username": "player1",
        "document": "player1",
        "password": "player123",
    },
    {
        "email": "player2@gmail.com",
        "username": "player2",
        "document": "player2",
        "password": "player123",
    },
    {
        "email": "player3@gmail.com",
        "username": "player3",
        "document": "player3",
        "password": "player123",
    },
    {
        "email": "player4@gmail.com",
        "username": "player4",
        "document": "player4",
        "password": "player123",
    },
    {
        "email": "player5@gmail.com",
        "username": "player5",
        "document": "player5",
        "password": "player123",
    },
    {
        "email": "player6@gmail.com",
        "username": "player6",
        "document": "player6",
        "password": "player123",
    },
    {
        "email": "player7@gmail.com",
        "username": "player7",
        "document": "player7",
        "password": "player123",
    },
    {
        "email": "player8@gmail.com",
        "username": "player8",
        "document": "player8",
        "password": "player123",
    },
    {
        "email": "player9@gmail.com",
        "username": "player9",
        "document": "player9",
        "password": "player123",
    },
    {
        "email": "player10@gmail.com",
        "username": "player10",
        "document": "player10",
        "password": "player123",
    },
    {
        "email": "player11@gmail.com",
        "username": "player11",
        "document": "player11",
        "password": "player123",
    },
    {
        "email": "player12@gmail.com",
        "username": "player12",
        "document": "player12",
        "password": "player123",
    },
]

def seed_users(stdout):
    for user_data in USERS:
        email = user_data["email"]

        if User.objects.filter(email=email).exists():
            stdout.write(f"⚠️ User {email} already exists")
            continue

        password = user_data.pop("password")

        user = User.objects.create_user(**user_data)
        user.set_password(password)
        user.save()

        stdout.write(f"✅ Created user {email}")

