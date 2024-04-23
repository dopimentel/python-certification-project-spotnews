from django.db import models
from news.validators import Validate


class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    role = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=200, validators=[Validate.two_words])
    content = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="news",
    )
    created_at = models.DateField()
    image = models.ImageField(upload_to="img/", null=True, blank=True)
    categories = models.ManyToManyField(Category, related_name="news")

    def __str__(self):
        return self.title
