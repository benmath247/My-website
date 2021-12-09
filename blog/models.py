from django.db import models
from django.template.defaultfilters import default, slugify
from ckeditor.fields import RichTextField
from datetime import datetime


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True, default="", max_length=100)
    image = models.ImageField(
        upload_to="static/images", null=True, blank=True, default=None
    )
    date_added = models.DateTimeField(default=datetime.now(), blank=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=250)
    intro = models.TextField(max_length=180)
    body = RichTextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(null=True, blank=True)
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.CASCADE
    )
    video = models.FileField(upload_to="static/videos/", null=True, verbose_name="")

    def slug(self):
        return slugify(self.title)

    class Meta:
        ordering = ["-date_added"]


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    comment = models.CharField(max_length=180)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_added"]
