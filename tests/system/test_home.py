from unittest import TestCase
from training_tracker.web_app import app
import json


class TestHome(TestCase):
    def test_home(self):
        with app.test_client() as client:
            response = client.get('/')

            self.assertEqual(response.status_code, 200)
            self.assertEqual(
                json.loads(response.get_data().decode('utf-8')),
                {'message': 'Hello world'}
            )
