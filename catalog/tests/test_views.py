from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from catalog.models import Genre, Translator

GENRE_LIST_URL = reverse("catalog:genre-list")
GENRE_CREATE_URL = reverse("catalog:genre-create")


class PublicGenreTests(TestCase):
    def test_login_required(self):
        resp = self.client.get(GENRE_CREATE_URL)

        self.assertNotEqual(resp.status_code, 200)

    def test_retrieve_genre_list(self):
        Genre.objects.create(name="Test", description="test")
        Genre.objects.create(name="Test2", description="test")

        resp = self.client.get(GENRE_LIST_URL)
        genres = Genre.objects.all()

        self.assertEqual(list(resp.context["genre_list"]), list(genres))

    def test_create_translator(self):
        form_data = {
            "username": "username",
            "password1": "123PassWord1234",
            "password2": "123PassWord1234",
            "language": "EN",
        }
        self.client.post(reverse("catalog:translator-create"), data=form_data)
        translator = Translator.objects.get(username=form_data["username"])

        self.assertEqual(translator.username, form_data["username"])
        self.assertTrue(translator.check_password(form_data["password1"]))
        self.assertEqual(translator.language, form_data["language"])


class PrivateGenreTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user("test", "Password1234")
        self.client.force_login(self.user)

    def test_login_required(self):
        resp = self.client.get(GENRE_CREATE_URL)

        self.assertEqual(resp.status_code, 200)

    def test_create_genre(self):
        form_data = {"name": "Test", "description": "test, test"}
        self.client.post(GENRE_CREATE_URL, data=form_data)
        genre = Genre.objects.get(name=form_data["name"])

        self.assertEqual(genre.name, form_data["name"])
        self.assertEqual(genre.description, form_data["description"])
