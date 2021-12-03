from django.shortcuts import redirect, render
from .models import Post, Comment
from .forms import CommentForm


def blog(request):
    posts = Post.objects.all()
    return render(request, "blog.html", {"posts": posts})


def post_detail(request, title):
    post = Post.objects.get(title=title)
    form = CommentForm
    return render(request, "post_detail.html", {"post": post, "comment_form": form})


def add_comment(request, title):
    if request.method == "GET":
        form = CommentForm()
        return render(request, "add_comment.html", context={"comment_form": form})

    if request.method == "POST":
        body = request.POST.get("body")
        post = Post.objects.get(title=title)
        Comment.objects.create(body=body, post=post)
        return redirect("home")


def home(request):
    return render(request, "home.html")


def contact(request):
    return render(request, "contact.html")
