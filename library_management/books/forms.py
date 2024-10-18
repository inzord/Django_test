from django import forms
from .models import Author, Book, Reader


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'is_available']


class ReaderForm(forms.ModelForm):
    class Meta:
        model = Reader
        fields = ['first_name', 'last_name', 'read_books']
