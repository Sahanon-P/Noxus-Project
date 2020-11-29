from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class AuthenticationTest(TestCase):
    """Test the authentication of user"""

    def setUp(self) :
        """Initailize the user for authentication testing."""
        User = get_user_model()
        user = User.objects.create_user("league of legend",
            email="riotCompany@gmail.com", password="TheBestGameMobaEver")
        user.first_name = "Ryze"
        user.last_name = "Tryndamere"
        user.save()

    def test_authenticated_user(self):
        """Test authenticated user that must response my_build page."""

        self.client.login(username="league of legend", password="TheBestGameMobaEver")
        response = self.client.get(reverse("my_build"))
        self.assertEqual(response.status_code, 200)

    # fix in view.py to redirect to 404 not found
    def test_unauthenticated_user(self):
        """Test unauthenticated user that must not response my_build page."""
        
        response = self.client.get(reverse("my_build"))
        self.assertEqual(response.status_code, 404)
