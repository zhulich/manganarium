from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from catalog.forms import TranslatorCreationFrom, MangaForm, MangaSearchForm, TranslatorSearchForm, \
    TranslatedMangaSearchForm, GenreSearchForm
from catalog.models import Translator, Manga, TranslatedManga, Genre


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
    queryset = Genre.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GenreListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = GenreSearchForm(initial={
            "name": name
        })

        return context

    def get_queryset(self):
        form = GenreSearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(name__icontains=form.cleaned_data["name"])

        return self.queryset


class GenreDetailView(generic.DetailView):
    model = Genre


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
    success_url = reverse_lazy("catalog:genre-list")


class MangaListView(generic.ListView):
    model = Manga
    queryset = Manga.objects.prefetch_related("genre")
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MangaListView, self).get_context_data(**kwargs)

        title = self.request.GET.get("title", "")

        context["search_form"] = MangaSearchForm(initial={
            "title": title
        })

        return context

    def get_queryset(self):
        form = MangaSearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(title__icontains=form.cleaned_data["title"])

        return self.queryset


class MangaDetailView(generic.DetailView):
    model = Manga


class MangaCreateView(LoginRequiredMixin, generic.CreateView):
    model = Manga
    form_class = MangaForm
    success_url = reverse_lazy("catalog:manga-list")


class MangaUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Manga
    form_class = MangaForm
    success_url = reverse_lazy("catalog:manga-list")


class MangaDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Manga
    success_url = reverse_lazy("catalog:manga-list")


class TranslatorListView(generic.ListView):
    model = Translator
    queryset = Translator.objects.all()
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TranslatorListView, self).get_context_data(**kwargs)

        username = self.request.GET.get("username", "")

        context["search_form"] = TranslatorSearchForm(initial={
            "username": username
        })

        return context

    def get_queryset(self):
        form = TranslatorSearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(
                username__icontains=form.cleaned_data["username"])

        return self.queryset


class TranslatorDetailView(generic.DetailView):
    model = Translator


class TranslatorCreateView(generic.CreateView):
    model = Translator
    form_class = TranslatorCreationFrom
    success_url = reverse_lazy("catalog:index")


class TranslatedMangaListView(generic.ListView):
    model = TranslatedManga
    template_name = "catalog/translated_manga_list.html"
    context_object_name = "translated_manga_list"
    queryset = TranslatedManga.objects.select_related("original_title", "translator")
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TranslatedMangaListView, self).get_context_data(**kwargs)

        translated_title = self.request.GET.get("translated_title", "")

        context["search_form"] = TranslatedMangaSearchForm(initial={
            "translated_title": translated_title
        })

        return context

    def get_queryset(self):
        form = TranslatedMangaSearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(
                translated_title__icontains=form.cleaned_data["translated_title"])

        return self.queryset


class TranslatedMangaDetailView(generic.DetailView):
    model = TranslatedManga
    template_name = "catalog/translated_manga_detail.html"
    context_object_name = "translated_manga_detail"


class TranslatedMangaCreateView(LoginRequiredMixin, generic.CreateView):
    model = TranslatedManga
    fields = "__all__"
    template_name = "catalog/translated_manga_form.html"
    success_url = reverse_lazy("catalog:translated-manga-list")


class TranslatedMangaUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TranslatedManga
    fields = "__all__"
    template_name = "catalog/translated_manga_form.html"
    success_url = reverse_lazy("catalog:translated-manga-list")


class TranslatedMangaDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TranslatedManga
    template_name = "catalog/translated_manga_confirm_delete.html"
    success_url = reverse_lazy("catalog:translated-manga-list")



