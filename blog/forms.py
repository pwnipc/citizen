from django import forms
from .models import Blog, Author

class BlogForm(forms.ModelForm):
    """Form for creating and updating blog posts"""
    
    class Meta:
        model = Blog
        fields = ['author', 'image', 'title', 'body']
