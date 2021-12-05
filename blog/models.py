from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(default="default")
    parent = models.ForeignKey(
        "self", blank=True, null=True, related_name="children", on_delete=models.CASCADE
    )

    class Meta:

        unique_together = (
            "slug",
            "parent",
        )
        verbose_name_plural = "categories"

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return " -> ".join(full_path[::-1])


class Post(models.Model):
    title = models.CharField(max_length=250)
    intro = models.TextField(max_length=180)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(null=True, blank=True)
    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.CASCADE
    )

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
