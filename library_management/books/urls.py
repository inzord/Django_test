from django.urls import path, include
from .views import (
    AuthorListView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView,
    BookListView, BookCreateView, BookUpdateView, BookDeleteView,
    ReaderListView, ReaderCreateView, ReaderUpdateView, ReaderDeleteView
)

urlpatterns = [
    path('authors/', AuthorListView.as_view(), name='author_list'),
    path('authors/create/', AuthorCreateView.as_view(), name='author_create'),
    path('authors/update/<int:pk>/', AuthorUpdateView.as_view(), name='author_update'),
    path('authors/delete/<int:pk>/', AuthorDeleteView.as_view(), name='author_delete'),

    path('', BookListView.as_view(), name='book_list'),
    path('add/', BookCreateView.as_view(), name='add_book'),
    path('update/<int:pk>/', BookUpdateView.as_view(), name='update_book'),
    path('delete/<int:pk>/', BookDeleteView.as_view(), name='delete_book'),

    path('readers/', ReaderListView.as_view(), name='reader_list'),
    path('readers/create/', ReaderCreateView.as_view(), name='reader_create'),
    path('readers/update/<int:pk>/', ReaderUpdateView.as_view(), name='reader_update'),
    path('readers/delete/<int:pk>/', ReaderDeleteView.as_view(), name='reader_delete'),
]
