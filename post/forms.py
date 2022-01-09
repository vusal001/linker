from django import forms
from django.forms import fields
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('link', 'title', 'category', 'image', 'linktype')

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        
        self.fields['image'].widget.attrs = {'class': 'w-75 font-italic pl-2 border-0 d-none', 'id':'book-image-upload'}
        self.fields['link'].widget.attrs = {'class': 'w-75 font-italic pl-2 border-0', 'border': 'none', 'placeholder': 'https://www.example.com/', 'rows': '1'}
        self.fields['title'].widget.attrs = {'class': 'w-75 font-italic pl-2 border-0', 'border': 'none', 'placeholder': 'Başlıq'}
        self.fields['category'].widget.attrs = {'class': 'insert-book_select font-italic pl-2 border-0 cursor-pointer', 'placeholder': 'Kategoriya'}
        self.fields['linktype'].widget.attrs = {'class': 'insert-book_select font-italic pl-2 border-0 cursor-pointer', 'placeholder': 'Sosial şəbəkə'}
        