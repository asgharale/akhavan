from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    meta = models.TextField(max_length=455, blank=True)
    thumbnail = models.ImageField(upload_to="sort/cat/%Y-%m/")

    def __str__(self) -> str:
        return self.name

class SubCategory(models.Model):
    parent = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    meta = models.TextField(max_length=455, blank=True)
    thumbnail = models.ImageField(upload_to="sort/cat/%Y-%m/")

    def __str__(self) -> str:
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name