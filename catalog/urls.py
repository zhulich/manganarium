from django.urls import path

from catalog.views import index, GenreListView, MangaListView, TranslatorListView, TranslatedMangaListView, \
    MangaDetailView, TranslatorDetailView, TranslatedMangaDetailView

urlpatterns = [
    path("", index, name="index"),
    path("genres/", GenreListView.as_view(), name="genre-list"),
    path("mangas/", MangaListView.as_view(), name="manga-list"),
    path("mangas/<int:pk>/", MangaDetailView.as_view(), name="manga-detail"),
    path("translators/", TranslatorListView.as_view(), name="translator-list"),
    path("translators/<int:pk>/", TranslatorDetailView.as_view(), name="translator-detail"),
    path("transleted/", TranslatedMangaListView.as_view(), name="translated-manga-list"),
    path("transleted/<int:pk>/", TranslatedMangaDetailView.as_view(), name="translated-manga-detail"),
]

app_name = "catalog"
