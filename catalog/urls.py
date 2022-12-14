from django.urls import path

from catalog.views import (
    index,
    GenreListView,
    MangaListView,
    TranslatorListView,
    TranslatedMangaListView,
    MangaDetailView,
    TranslatorDetailView,
    TranslatedMangaDetailView,
    GenreCreateView,
    GenreUpdateView,
    GenreDeleteView,
    TranslatorCreateView,
    MangaCreateView,
    MangaUpdateView,
    MangaDeleteView,
    TranslatedMangaCreateView,
    TranslatedMangaUpdateView,
    TranslatedMangaDeleteView,
    GenreDetailView,
)

urlpatterns = [
    path("", index, name="index"),
    path("genres/", GenreListView.as_view(), name="genre-list"),
    path("genres/create/", GenreCreateView.as_view(), name="genre-create"),
    path("genre/<int:pk>/", GenreDetailView.as_view(), name="genre-detail"),
    path("genres/<int:pk>/update/", GenreUpdateView.as_view(), name="genre-update"),
    path("genres/<int:pk>/delete/", GenreDeleteView.as_view(), name="genre-delete"),
    path("mangas/", MangaListView.as_view(), name="manga-list"),
    path("mangas/create/", MangaCreateView.as_view(), name="manga-create"),
    path("mangas/<int:pk>/", MangaDetailView.as_view(), name="manga-detail"),
    path("mangas/<int:pk>/update/", MangaUpdateView.as_view(), name="manga-update"),
    path("mangas/<int:pk>/delete/", MangaDeleteView.as_view(), name="manga-delete"),
    path("translators/", TranslatorListView.as_view(), name="translator-list"),
    path("registrarion/", TranslatorCreateView.as_view(), name="translator-create"),
    path(
        "translators/<int:pk>/",
        TranslatorDetailView.as_view(),
        name="translator-detail",
    ),
    path(
        "transleted/", TranslatedMangaListView.as_view(), name="translated-manga-list"
    ),
    path(
        "transleted/create/",
        TranslatedMangaCreateView.as_view(),
        name="translated-manga-create",
    ),
    path(
        "transleted/<int:pk>/",
        TranslatedMangaDetailView.as_view(),
        name="translated-manga-detail",
    ),
    path(
        "transleted/<int:pk>/update/",
        TranslatedMangaUpdateView.as_view(),
        name="translated-manga-update",
    ),
    path(
        "transleted/<int:pk>/delete/",
        TranslatedMangaDeleteView.as_view(),
        name="translated-manga-delete",
    ),
]

app_name = "catalog"
