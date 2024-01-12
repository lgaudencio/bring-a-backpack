from django.test import TestCase


class TestViews(TestCase):
    """
    Test Reviewsite app
    """
    def test_home_page(self):
        """ Test that the home page renders correctly """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviewsite/index.html')