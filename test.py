import unittest
from server import app
import json
from flask import Flask, render_template, redirect, request, flash, session
from model import connect_to_db, db

class RouteTest(unittest.TestCase):
    """Tests routes"""

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = "ABC"
        connect_to_db(app)
        with self.client.session_transaction() as session:
            session["user_id"] = 1


    def tearDown(self):
        pass

    def test_homepage(self):
        result = self.client.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn("Pretty placeholder", result.data)

    def test_profilepage(self):
        result = self.client.get('/profile')
        self.assertEqual(result.status_code, 200)
        self.assertIn("'s Trips", result.data)

    def test_settingspage(self):
        result = self.client.get('/settings')
        self.assertEqual(result.status_code, 200)
        self.assertIn("All da Settings!", result.data)

    def login(self, email, user_password):
        return self.client.post('/login', data=
            {"email":email,
            "user-password":user_password},
            follow_redirects=True)

    def logout(self):
        return self.client.get('/logout', follow_redirects=True)

    def test_login_logout(self):
        result = self.login('minyisme@gmail.com', 'abc123')
        self.assertEqual(result.status_code, 200)
        assert "minyisme" in result.data
        result = self.logout()
        self.assertEqual(result.status_code, 200)
        assert "Pretty placeholder" in result.data

    def test_user_reg_form(self):
        result = self.client.get('/user-reg-form')
        self.assertIn("Email", result.data)

    def user_registration(self, useremail, userpassword, username, originairportcode):
        return self.client.post('/user-registration', data={"user-email":useremail, 
            "user-password":userpassword, 
            "username":username, 
            "origin_airport_code":originairportcode },
            follow_redirects=True)

    def test_user_registration(self):
        result = self.user_registration('minyisme@gmail.com', 'abc123', 'minyisme', 'SFO')
        self.assertEqual(result.status_code, 200)
        assert "Pretty placeholder" in result.data

    # WORKS BUT COMMENTED OUT BECAUSE CHANGES MY DB


    # def trip_create(self, tripname):
    #     return self.client.post('/trip/create-new', 
    #         data={"trip_name": tripname},
    #         follow_redirects=True)

    # def test_trip_create(self):
    #     result = self.trip_create('Testing Test to Test')
    #     self.assertEqual(result.status_code, 200)
    #     assert "Testing Test to Test" in result.data

    # def trip_delete(self, tripid):
    #     return self.client.post('/profile/trip-delete',
    #         data={"trip-id-delete": tripid},
    #         follow_redirects=True)

    # def test_trip_delete(self):
    #     result = self.trip_delete(21)
    #     self.assertEqual(result.status_code, 200)
    #     assert "'s Trips" in result.data

    def test_trip(self):
        result = self.client.get('/trip/11')
        self.assertIn("All the infos!", result.data)

    # def test_trip_search(self, trip_id):
    #     result = self.client.get('/trip/<int:trip_id>/search')
    #     self.assertIn("All the Searchings!", result.data)

    # def test_trip_results(self):
    #     result = self.client.get('/trip/<int:trip_id>/results')
    #     self.assertIn("Destination", result.data)

    # def test_trip_share(self):
    #     result = self.client.get('/trip/<int:trip_id>/share')
    #     self.assertIn("infos here to share", result.data)

if __name__ == "__main__":
    
    unittest.main()


