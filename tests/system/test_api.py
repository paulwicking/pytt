from unittest import TestCase
from training_tracker.web_app import app
from training_tracker import MODULE_NAME, MODULE_VERSION
import json


class TestAPI(TestCase):
    """Tests for the API interface."""
    def test_api_home(self):
        with app.test_client() as client:
            response = client.get('/api/')

            self.assertEqual(response.status_code, 200)
            self.assertEqual(
                #  Remember to decode to UTF-8 for Python 3.4 and 3.5
                json.loads(response.get_data().decode('utf-8')),
                {'message': '%s %s API' % (MODULE_NAME, MODULE_VERSION)}
            )
