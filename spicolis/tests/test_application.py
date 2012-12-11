import unittest

from spicolis import create_application


class AppRoutingTestCase(unittest.TestCase):

    def test_index_page(self):
        """Ensure that the index page is loaded correctly"""
        app = create_application().test_client()
        rv = app.get('/')

        self.assertEqual(rv.data, "")
