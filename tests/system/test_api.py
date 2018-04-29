from unittest import TestCase
from training_tracker import MODULE_NAME, MODULE_VERSION
from training_tracker.web_app.api import app
import json


class TestAPI(TestCase):
    """Tests for the API interface."""
    def test_api_home(self):
        with app.test_client() as client:
            expected_status = 200
            expected_data = {
                'message': '%s %s API' % (MODULE_NAME, MODULE_VERSION)
            }

            response = client.get('/api/')

            self.assertEqual(expected_status, response.status_code)
            #  Remember to decode json loaded response to UTF-8 for Python 3.4 and 3.5
            self.assertEqual(expected_data, json.loads(response.get_data().decode('utf-8')))
