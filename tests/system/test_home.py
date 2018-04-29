# from unittest import TestCase
# from training_tracker.web_app.api import app
# import json
#
#
# class TestHome(TestCase):
#     def test_home(self):
#         with app.test_client() as client:
#             expected_status = 200
#             expected_data = {'message': 'Hello world'}
#             response = client.get('/')
#
#             self.assertEqual(expected_status, response.status_code)
#             #  Remember to decode json loaded response to UTF-8 for Python 3.4 and 3.5
#             self.assertEqual(expected_data, json.loads(response.get_data().decode('utf-8')))
