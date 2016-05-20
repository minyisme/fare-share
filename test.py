import unittest
from server import app

class RouteTest(unittest.TestCase):
    """Tests routes"""

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        result = self.client.get('/')
        self.assertIn("Pretty placeholder", result.data)

    def test_profilepage(self):
        result = self.client.get('/profile')
        self.assertIn("Travels and Stuffs", result.data)

    def test_settingspage(self):
        result = self.client.get('/settings')
        self.assertIn("All da Settings!", result.data)

    def test_trippage(self):
        result = self.client.get('/trip')
        self.assertIn("Trip: All the infos!", result.data)

    def test_searchpage(self):
        result = self.client.get('/trip/search')
        self.assertIn("All the Searchings!", result.data)

    def test_resultspage(self):
        result = self.client.get('/trip/results')
        self.assertIn("Flight infos here!", result.data)

    def test_sharepage(self):
        result = self.client.get('/trip/share')
        self.assertIn("Flight infos here to share!", result.data)

if __name__ == "__main__":
    
    unittest.main()