from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Photography
import tempfile


class TestViews(TestCase):
    """
    Test cases for photography app as logged in user
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

        # Create photography post
        photography = Photography.objects.create(
            user=self.user,
            post_title="City, Country",
            post_brief="A little description",
            main_photo=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            main_photo_alt="A test image",
            photo_1=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            photo_1_alt="A test image",
            photo_2=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            photo_2_alt="A test image",
            photo_3=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            photo_3_alt="A test image",
            photo_4=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            photo_4_alt="A test image",
            photo_5=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            photo_5_alt="A test image",
            photo_6=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            photo_6_alt="A test image",
            photo_7=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            photo_7_alt="A test image",
            photo_8=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            photo_8_alt="A test image",
            photo_9=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            photo_9_alt="A test image",
            )

    def test_create_photography_post_page(self):
        """ Create photography post when logged in """
        response = self.client.get('/photography/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'photography/add_photography.html')


class TestViewsRedirect(TestCase):
    """
    Test views when not logged in
    """
    def test_create_photography_post_redirect(self):
        """ Create photography post test """
        response = self.client.get('/photography/')
        self.assertEqual(response.status_code, 302)

    def test_edit_photography_post_redirect(self):
        """ Edit photography post test """
        response = self.client.get('/photography/edit/5/')
        self.assertEqual(response.status_code, 302)

    def test_delete_photography_post_redirect(self):
        """ Delete photography post test """
        response = self.client.get('/photography/delete/5/')
        self.assertEqual(response.status_code, 302)
