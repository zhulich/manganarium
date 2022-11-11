from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=63, unique=True)
    description = models.TextField()

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Translator(AbstractUser):
    language = models.CharField(max_length=255)

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return f"{self.username}({self.language})"


class Manga(models.Model):
    title = models.CharField(max_length=63, unique=True)
    mangaka = models.CharField(max_length=255)
    year = models.DateField(validators=[MinValueValidator(1950), MaxValueValidator(2023)])
    chapters = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    genre = models.ManyToManyField(Genre, related_name="genres")
    translator = models.ManyToManyField(Translator, related_name="translators")

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"{self.title}, {self.year}"


class TranslatedManga(models.Model):
    translated_title = models.CharField(max_length=255, unique=True)
    original_title = models.ForeignKey(to=Manga, on_delete=models.SET("unknown"), related_name="original", null=True)
    translator = models.ForeignKey(to=Translator, on_delete=models.SET("unknown"), related_name="translator", null=True)

    def __str__(self):
        return self.translated_title


