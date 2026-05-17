import unittest
from hello_world import app
from hello_world.formater import SUPPORTED


class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        for s in SUPPORTED:
            self.assertIn(s.encode(), rv.data)

    def test_msg_with_output_json(self):
        rv = self.app.get('/?output=json')
        self.assertEqual(b'{ "imie":"Ivo", "msg":"Hello World!"}', rv.data)
