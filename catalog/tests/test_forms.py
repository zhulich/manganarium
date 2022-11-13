from django.test import TestCase

from catalog.forms import TranslatorCreationFrom


class FormsTests(TestCase):
    def test_translator_creation_language_valid(self):
        form_data = {
            "username": "username",
            "password1": "123PassWord1234",
            "password2": "123PassWord1234",
            "language": "EN"
        }
        form = TranslatorCreationFrom(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_translator_creation_language_invalid(self):
        form_data = {
            "username": "username",
            "password1": "123PassWord1234",
            "password2": "123PassWord1234",
            "language": "UA"
        }
        form = TranslatorCreationFrom(data=form_data)
        self.assertFalse(form.is_valid())


