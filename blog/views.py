from django.shortcuts import render
from .models import Post


def blog(request):
    posts = Post.objects.all()
    return render(request, "blog.html", {"posts": posts})


def post_detail(request, title):
    post = Post.objects.get(title=title)
    return render(request, "post_detail.html", {"post": post})


def home(request):
    return render(request, "home.html")


def contact(request):
    return render(request, "contact.html")
