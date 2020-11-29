from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.FireFox.options import Options

class SearchTest(TestCase) :
    """Testing search bar."""
    
    def test_search_bar(self):
        """test search bar efficeincy as mush as possible."""

        option = Options()
        option.headless = True
        driver = webdriver.Firefox(options=option)
        driver.get("https://noxus-project.herokuapp.com/?search=Aatrox")
        links = driver.find_element_by_class_name("container")
        links2 = links.find_element_by_class_name("box")
        links3 = links2.find_element_by_tag_name("a")
        result = links3.get_attribute("href")
        driver.close()
        self.assertTrue("Aatrox" in result)
