from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from catalog.models import Translator, Manga, Genre, TranslatedManga


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


class MangaSearchForm(forms.Form):
    title = forms.CharField(
        max_length=63,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by title..."})
    )


class TranslatedMangaSearchForm(forms.Form):
    translated_title = forms.CharField(
        max_length=63,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by title..."})
    )


class TranslatorSearchForm(forms.Form):
    username = forms.CharField(
        max_length=63,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by nickname..."})
    )


class GenreSearchForm(forms.Form):
    name = forms.CharField(
        max_length=63,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by genre..."})
    )