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

    # def test_logout(self):
    #     result = self.client.get('/logout')
    #     self.assertIn("change this!!!!!", result.data)

    def test_user_reg_form(self):
        result = self.client.get('/user-reg-form')
        self.assertIn("Email", result.data)

    # def test_user_registration(self):
    #     result = self.client.get('/user-registration')
    #     self.assertIn("change this!!!!!", result.data)

    def test_trip_add(self):
        result = self.client.get('/trip/add')
        self.assertIn("Add up to 4 other users to this trip", result.data)

    # def test_trip_create(self):
    #     result = self.client.get('/trip/create_new')
    #     self.assertIn("change this!!!!!", result.data)

    # def test_trip(self, trip_id):
    #     result = self.client.get('/trip/<int:trip_id>')
    #     self.assertIn("All the infos!", result.data)

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


