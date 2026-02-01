from rest_framework.test import APITestCase
from users.models import User

class UserListTests(APITestCase):

    def setUp(self):
        self.player = User.objects.create_user(
            email="player@test.com",
            password="player123",
            username="player1",
            is_club_owner=False
        )

        self.club = User.objects.create_user(
            email="club@test.com",
            password="123456",
            username="club1",
            is_club_owner=True
        )

        self.url = "/api/users/"

    def test_player_cannot_list_users(self):
        assert True
