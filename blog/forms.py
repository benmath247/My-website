from django import forms
from .models import Comment
from captcha.fields import CaptchaField


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email_address = forms.EmailField(max_length=150)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)
    captcha = CaptchaField()


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]
