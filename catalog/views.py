from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic

from catalog.models import Translator, Manga, TranslatedManga, Genre


# Create your views here.

def index(request):
    """View function for the home page of the site."""

    num_genre = Genre.objects.count()
    num_translator = Translator.objects.count()
    num_manga = Manga.objects.count()
    num_translated = TranslatedManga.objects.count()

    num_visits = request.session.get("num_visits", 1)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_genre": num_genre,
        "num_translator": num_translator,
        "num_manga": num_manga,
        "num_translated": num_translated,
        "num_visits": num_visits,
    }

    return render(request, "catalog/index.html", context=context)


class GenreListView(generic.ListView):
    model = Genre
    paginate_by = 2


class GenreCreateView(LoginRequiredMixin, generic.CreateView):
    model = Genre
    fields = "__all__"
    success_url = reverse_lazy("catalog:genre-list")


class GenreUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Genre
    fields = "__all__"
    success_url = reverse_lazy("catalog:genre-list")


class GenreDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Genre
    fields = "__all__"
    success_url = reverse_lazy("catalog:genre-list")


class MangaListView(generic.ListView):
    model = Manga
    queryset = Manga.objects.prefetch_related("genre")


class MangaDetailView(generic.DetailView):
    model = Manga


class TranslatorListView(generic.ListView):
    model = Translator
#    queryset = Translator.objects.select_related("translated")


class TranslatorDetailView(generic.DetailView):
    model = Translator


class TranslatedMangaListView(generic.ListView):
    model = TranslatedManga
    template_name = "catalog/translated_manga_list.html"
    context_object_name = "translated_manga_list"
    queryset = TranslatedManga.objects.select_related("original_title", "translator")


class TranslatedMangaDetailView(generic.DetailView):
    model = TranslatedManga
    template_name = "catalog/translated_manga_detail.html"
    context_object_name = "translated_manga_detail"
