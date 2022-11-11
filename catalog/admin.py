from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from catalog.models import Genre, Translator, Manga, TranslatedManga


@admin.register(Genre)
# Register your models here.
class GenreAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]


@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    list_display = ["title", "mangaka", "year", "chapters"]
    list_filter = ["mangaka", "year", "genre"]
    search_fields = ["title"]


@admin.register(TranslatedManga)
class TranslatedMangaAdmin(admin.ModelAdmin):
    list_display = ["translated_title", "original_title", "translator"]
    list_filter = ["translator"]
    search_fields = ["translated_title"]


@admin.register(Translator)
class TranslatorAdmin(UserAdmin):
    list_display = ("username", "email", "is_staff", "language")
    fieldsets = UserAdmin.fieldsets + (("Additional info", {"fields": ("language",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (("Additional info", {"fields": ("language", "first_name", "last_name")}),)


