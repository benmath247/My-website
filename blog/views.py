from django.shortcuts import redirect, render
from .models import Category, Post, Comment
from .forms import CommentForm, ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                "first_name": form.cleaned_data["first_name"],
                "last_name": form.cleaned_data["last_name"],
                "email": form.cleaned_data["email_address"],
                "message": form.cleaned_data["message"],
            }
            message = "\n".join(body.values())

            try:
                send_mail(
                    subject,
                    message,
                    "ben@employbenmath.com",
                    ["ben@employbenmath.com"],
                )
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("home")
        else:
            return redirect("contact")

    form = ContactForm()
    return render(request, "contact.html", {"form": form})


def blog(request):
    posts = Post.objects.all()
    return render(request, "blog.html", {"posts": posts})


def category(request):
    categories = Category.objects.all()
    return render(request, "home.html", {"categories": categories})


def post_detail(request, title):
    post = Post.objects.get(title=title)
    form = CommentForm
    return render(request, "post_detail.html", {"post": post, "comment_form": form})


def add_comment(request, title):
    if request.method == "GET":
        form = CommentForm()
        return render(request, "add_comment.html", context={"comment_form": form})

    if request.method == "POST":
        comment = request.POST.get("comment")
        post = Post.objects.get(title=title)
        Comment.objects.create(comment=comment, post=post)
        return redirect("home")


def home(request):
    return render(request, "home.html")
