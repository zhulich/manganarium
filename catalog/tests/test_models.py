from django.core.exceptions import ValidationError
from django.test import TestCase

from catalog.models import Genre, Translator, Manga, TranslatedManga


class GenreTests(TestCase):
    def test_manufacturer_str(self):
        genre = Genre.objects.create(
            name="genre",
            description="description"
        )
        self.assertEqual(str(genre), genre.name)

    def test_translator_str(self):
        translator = Translator.objects.create_user(
            username="test",
            password="test1234",
            language="language",
        )
        self.assertEqual(str(translator),
                         f"{translator.username}("
                         f"{translator.language})")

    def test_manga_str(self):
        genre1 = Genre.objects.create(
            name="genre1",
            description="description1"
        )
        genre2 = Genre.objects.create(
            name="genre2",
            description="description2"
        )
        genres = (genre1, genre2)
        manga = Manga.objects.create(title="test", year=2011, mangaka="Mangaka test", chapters=43)
        manga.genre.set(genres)

        self.assertEqual(str(manga), f"{manga.title}, {manga.year}")

    def test_create_translator_with_correct_language(self):
        username = "test"
        password = "Test1234"
        language = "EN"
        translator = Translator.objects.create_user(
            username=username,
            password=password,
            language=language,
        )

        self.assertEqual(translator.username, username)
        self.assertTrue(translator.check_password(password))
        self.assertTrue(translator.language, language)

    def test_translated_manga_str(self):
        genre = Genre.objects.create(
            name="genre",
            description="description"
        )
        translator = Translator.objects.create_user(
            username="test",
            password="test1234",
            language="language",
        )
        manga = Manga.objects.create(title="test", year=2011, mangaka="Mangaka test",
                                     chapters=43)
        manga.genre.set((genre,))
        translated_manga = TranslatedManga.objects.create(translated_title="test_translated", original_title=manga, translator=translator)

        self.assertEqual(str(translated_manga), translated_manga.translated_title)