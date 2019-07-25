from django.forms import ModelForm, Form
from .models import Blog

class BlogPost(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body']