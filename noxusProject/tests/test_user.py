from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from noxusProject.models import *

class UserTest(TestCase) :
    """Testing user feature."""
    
    def setUp(self):
        """Initailize the user for user feature testing."""

        User = get_user_model()
        user = User.objects.create_user("league of legend",
            email="riotCompany@gmail.com", password="TheBestGameMobaEver")
        user.first_name = "Ryze"
        user.last_name = "Tryndamere"
        user.save()
        self.client.login(username="league of legend", password="TheBestGameMobaEver")

        # demo champion for testing
        s = Spell.objects.create()
        champ = Champion.objects.create(name="Viktor",spell=s)
        item = ItemChampion.objects.create(name="Viktor")
        rune = RuneChampion.objects.create(name="Viktor")
        summonner_spell = RuneChampion.objects.create(name="Viktor")

    def test_detail_user_page(self):
        """test detail user page that redirect from user build page."""

        response = self.client.get(reverse("my_build"))
        self.assertEqual(response.status_code, 200)
