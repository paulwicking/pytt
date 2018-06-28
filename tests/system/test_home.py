from unittest import TestCase
from pytt.web_app import app
import json


class TestHome(TestCase):
    def test_home(self):
        with app.test_client() as client:
            response = client.get('/')

            self.assertEqual(response.status_code, 200)
            self.assertEqual(
                #  Remember to decode to UTF-8 for Python 3.4 and 3.5
                json.loads(response.get_data().decode('utf-8')),
                {'message': 'Hello world'}
            )
