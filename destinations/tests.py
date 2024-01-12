from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Destination
import tempfile


class TestViews(TestCase):
    """
    Test cases for destinations app as logged in user
    """
    def setUp(self):
        """ Setup test """
        username = "LFG"
        password = "Benfica24"
        user_model = get_user_model()

        # Create user
        self.user = user_model.objects.create_user(
            username=username,
            password=password,
            is_superuser=True
        )
        logged_in = self.client.login(username=username, password=password)
        self.assertTrue(logged_in)

        # Create destination review
        destination = Destination.objects.create(
            user=self.user,
            title="City, Country",
            brief="A little description",
            photo=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            photo_alt="A test image",
            review="A review about the city, country mentioned in title",
            )

    def test_create_destination_review_page(self):
        """ Create destination review when logged in """
        response = self.client.get('/destinations/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'destinations/add_destination.html')

    def test_edit_destination_review_page(self):
        """ Edit destination review when logged in """
        response = self.client.get('/destinations/edit/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'destinations/edit_destination.html')

    def test_delete_destination_review_page(self):
        """ Delete destination review when logged in """
        response = self.client.get('/destinations/delete/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'destinations/destination_confirm_delete.html'
        )

    def test_edit_review_unauthorized(self):
        """
        Test that another user cannot edit
        another users destination review
        """
        user_model = get_user_model()
        # Create second user for 403 errors
        username = 'LFilipe'
        password = 'gaudencio95'
        user = user_model.objects.create_user(
            username=username,
            password=password,
            is_superuser=False
        )
        logged_in = self.client.login(
            username=username,
            password=password
        )

        self.assertTrue(logged_in)
        response = self.client.get('/destinations/edit/1/')
        self.assertEqual(response.status_code, 403)

    def test_delete_review_unauthorized(self):
        """
        Test that another user cannot delete
        another users destination review
        """
        user_model = get_user_model()
        # Create second user for 403 errors
        username = 'LFilipe'
        password = 'gaudencio95'
        user = user_model.objects.create_user(
            username=username,
            password=password,
            is_superuser=False
        )
        logged_in = self.client.login(
            username=username,
            password=password
        )

        self.assertTrue(logged_in)
        response = self.client.get('/destinations/delete/1/')
        self.assertEqual(response.status_code, 403)


class TestViewsRedirect(TestCase):
    """
    Test views when not logged in
    """
    def test_create_destination_review_redirect(self):
        """ Create destination review test """
        response = self.client.get('/destinations/')
        self.assertEqual(response.status_code, 302)

    def test_edit_destination_review_redirect(self):
        """ Edit destination review test """
        response = self.client.get('/destinations/edit/1/')
        self.assertEqual(response.status_code, 302)

    def test_delete_destination_review_redirect(self):
        """ Delete destination review test """
        response = self.client.get('/destinations/delete/1/')
        self.assertEqual(response.status_code, 302)
