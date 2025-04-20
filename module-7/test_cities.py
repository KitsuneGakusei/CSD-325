# test_cities.py

import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_name = city_country("tokyo", "japan")
        self.assertEqual(formatted_name, "Tokyo, Japan")
        
unittest.main()
