from django import forms
from django.contrib.auth.forms import UserCreationForm
from catalog.models import Translator, Manga, Genre


class TranslatorCreationFrom(UserCreationForm):
    class Meta:
        model = Translator
        fields = UserCreationForm.Meta.fields + ("language",)


class MangaForm(forms.ModelForm):
    genre = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    year = forms.CharField(
        required=False
    )
    chapters = forms.CharField(
        required=False
    )

    class Meta:
        model = Manga
        fields = "__all__"