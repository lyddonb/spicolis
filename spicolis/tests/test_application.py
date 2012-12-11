import unittest

from spicolis import create_application


class AppRoutingTestCase(unittest.TestCase):

    def test_index_page(self):
        """Ensure that the index page returns no content"""
        app = create_application().test_client()
        index_page = app.get('/')

        self.assertEqual(index_page.data, "")

    def test_events_page(self):
        """Ensure that the events page returns no content"""
        app = create_application().test_client()
        event_page = app.get('/events')

        self.assertEqual(event_page.data, "")

    def test_specials_page(self):
        """Ensure that the specials page returns no content"""
        app = create_application().test_client()
        specials_page = app.get('/specials')

        self.assertEqual(specials_page.data, "")

    def test_about_page(self):
        """Ensure that the about page returns no content"""
        app = create_application().test_client()
        about_page = app.get('/about')

        self.assertEqual(about_page.data, "")
