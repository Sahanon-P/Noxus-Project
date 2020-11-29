from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class DetailPageTest(TestCase) :
    """Testing detail page and detail user page."""

    def test_detail_page(self):
        """test detail page that redirect from index page."""
        
        option = webdriver.ChromeOptions()
        option.add_argument("headless")
        driver = webdriver.Chrome(options=option)
        driver.get("https://noxus-project.herokuapp.com/champion/Fizz")
        link = driver.find_element_by_class_name("grid-container")
        link2 = link.find_element_by_class_name("banner")
        result = link2.find_element_by_class_name("champion_name").text
        driver.close()
        self.assertEqual(result, "Fizz")
