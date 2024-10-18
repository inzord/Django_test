from django.contrib import admin
from .models import Author, Book, Reader

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Reader)
