from django.test import TestCase
from django.urls import reverse


class IndexPageTest(TestCase) :
    """Testing index page test."""
    
    def test_index_page_responsed(self):
        """test the index page could responsed."""
        response = self.client.get(reverse('noxusProject:index'))
        self.assertEqual(response.status_code, 200)