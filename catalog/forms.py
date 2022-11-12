from django.contrib.auth.forms import UserCreationForm
from catalog.models import Translator


class TranslatorCreationFrom(UserCreationForm):
    class Meta:
        model = Translator
        fields = UserCreationForm.Meta.fields + ("language",)