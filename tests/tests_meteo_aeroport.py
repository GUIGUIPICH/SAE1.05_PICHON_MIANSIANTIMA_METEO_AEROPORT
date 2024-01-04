import unittest
from meteo_aeroport import *

class TestWeatherFunctions(unittest.TestCase):
    def test_site_allmetsat(self):
        result = site_allmetsat("LFBI")
        self.assertIsInstance(result, str)

    def test_site_meteoblue(self):
        result = site_meteoblue("LFBI")
        self.assertIsInstance(result, str)

    def test_weathertoday(self):
        site_allmetsat_url = site_allmetsat("LFBI")
        result = weathertoday(site_allmetsat_url)
        self.assertIsInstance(result, tuple)
        # Ajoutez d'autres assertions en fonction de la structure du résultat

    def test_weatherforecast(self):
        site_meteoblue_url = site_meteoblue("LFBI")
        result = weatherforecast(1, site_meteoblue_url)
        self.assertIsInstance(result, tuple)
        # Ajoutez d'autres assertions en fonction de la structure du résultat

    def test_time_1(self):
        result = time_1()
        self.assertIsInstance(result, str)

if __name__ == '__main__':
    unittest.main()






