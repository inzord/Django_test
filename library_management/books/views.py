from django.db.models import Q
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Author, Book, Reader
from .forms import AuthorForm, BookForm, ReaderForm


# Author Views
class AuthorListView(ListView):
    model = Author
    template_name = 'books/author_list.html'
    context_object_name = 'authors'


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'books/author_form.html'
    success_url = reverse_lazy('author_list')


class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'books/author_form.html'
    success_url = reverse_lazy('author_list')


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'books/author_confirm_delete.html'
    success_url = reverse_lazy('author_list')


# Book Views

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        queryset = super().get_queryset()
        author_filter = self.request.GET.get('author', '')
        if author_filter:
            queryset = queryset.filter(
                Q(author__first_name__icontains=author_filter) |
                Q(author__last_name__icontains=author_filter)
            )
        return queryset


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/add_book.html'
    success_url = reverse_lazy('book_list')


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/update_book.html'
    success_url = reverse_lazy('book_list')


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/delete_book.html'
    success_url = reverse_lazy('book_list')


# Reader Views
class ReaderListView(ListView):
    model = Reader
    template_name = 'books/reader_list.html'
    context_object_name = 'readers'


class ReaderCreateView(CreateView):
    model = Reader
    form_class = ReaderForm
    template_name = 'books/reader_form.html'
    success_url = reverse_lazy('reader_list')


class ReaderUpdateView(UpdateView):
    model = Reader
    form_class = ReaderForm
    template_name = 'books/reader_form.html'
    success_url = reverse_lazy('reader_list')


class ReaderDeleteView(DeleteView):
    model = Reader
    template_name = 'books/reader_confirm_delete.html'
    success_url = reverse_lazy('reader_list')
