import unittest
import json
from app import app 

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_case_1(self):
        payload = {'a': 5, 'b': 6, 'operator': "+"}
        response = self.app.post('/lab15/operation/', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['result'], "11")

    def test_case_2(self): 
        payload = {'a': 17, 'b': 9, 'operator': "-"}
        response = self.app.post('/lab15/operation/', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['result'], "8")

    def test_case_3(self): 
        payload = {'a': 3, 'b': 7, 'operator': "*"}
        response = self.app.post('/lab15/operation/', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['result'], "uildlee zov oruulna uu!")