from django import forms
from django.core.exceptions import ValidationError
from .models import Author, Tag, Catagory, Post,Contact
from django.template.defaultfilters import slugify

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','content', 'author', 'catagory', 'tags')


    def clean_name(self):
        name = self.cleaned_data['title']

        if name.lower()== 'post' or name.lower() == "add" or name.lower() == 'update':
            raise  ValidationError("Post name cann't be '{}'".format(name))
        return name

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = "__all__"

