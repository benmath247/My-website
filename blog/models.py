from django.db import models
from django.template.defaultfilters import slugify


class Post(models.Model):
    title = models.CharField(max_length=250)
    intro = models.TextField(max_length=180)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def slug(self):
        return slugify(self.title)

    class Meta:
        ordering = ["-date_added"]
