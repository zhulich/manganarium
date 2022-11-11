from django.shortcuts import render
from django.views import generic

from catalog.models import Translator, Manga, TranslatedManga, Genre


# Create your views here.

def index(request):
    """View function for the home page of the site."""

    num_genre = Genre.objects.count()
    num_translator = Translator.objects.count()
    num_manga = Manga.objects.count()
    num_translated = TranslatedManga.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_genre": num_genre,
        "num_translator": num_translator,
        "num_manga": num_manga,
        "num_translated": num_translated,
        "num_visits": num_visits + 1,
    }

    return render(request, "catalog/index.html", context=context)


class GenreListView(generic.ListView):
    model = Genre
