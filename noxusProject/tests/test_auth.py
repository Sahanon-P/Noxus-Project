from django.test import TestCase
from django.contrib.auth.models import User


class AuthenticationTest(TestCase):
    """Test the authentication of user"""

    def setUp(self) :
        """Initailize the user for authentication testing."""

        user = User.objects.create_user("league of legend",
            email="riotCompany@gmail.com", password="TheBestGameMobaEver")
        user.first_name = "Ryze"
        user.last_name = "Tryndamere"
        user.save()

    def test_authenticated_user(self):
        # waiting for create_build page
        pass

    def test_unauthenticated_user(self):
        #  waiting for create_build page 
        pass
