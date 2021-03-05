from django import forms
from django.forms import ModelForm
from .models import ContactEnty, Comment, Subscribe



class Contacform(ModelForm):
    email = forms.EmailField()

    class Meta:
        model = ContactEnty
        fields = ['name', 'email', 'phone', 'subject', 'message',]


class Commentform(ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Comment
        fields = ['name', 'email', 'comment_body']



class subform(ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Subscribe
        fields = ['email']