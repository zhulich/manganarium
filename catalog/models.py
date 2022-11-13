from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import UniqueConstraint


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=63, unique=True)
    description = models.TextField()

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Translator(AbstractUser):
    LANGUAGES = [
        ("EN", "english"),
        ("FR", "french"),
        ("GE", "german"),
        ("ES", "spanish")
    ]
    language = models.CharField(max_length=255, choices=LANGUAGES)

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return f"{self.username}({self.language})"


class Manga(models.Model):
    title = models.CharField(max_length=63, unique=True)
    mangaka = models.CharField(max_length=255)
    year = models.IntegerField(validators=[MinValueValidator(1950), MaxValueValidator(2030)])
    chapters = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    genre = models.ManyToManyField(Genre, related_name="mangas")

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"{self.title}, {self.year}"


class TranslatedManga(models.Model):
    translated_title = models.CharField(max_length=255, unique=True)
    original_title = models.ForeignKey(to=Manga, on_delete=models.SET("unknown"), related_name="original", null=True)
    translator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET("unknown"), related_name="translated", null=True)

    class Meta:
        constraints = (models.UniqueConstraint(fields=["original_title", "translator"], name="unique_translate"),)

    def __str__(self):
        return self.translated_title


