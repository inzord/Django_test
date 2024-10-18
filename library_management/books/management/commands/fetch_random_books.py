import datetime

import requests
from django.core.management.base import BaseCommand
from books.models import Author, Book


class Command(BaseCommand):
    help = 'Fetch random books from Google Books API and save them to the database'

    def handle(self, *args, **kwargs):
        url = f'https://www.googleapis.com/books/v1/volumes/s1gVAAAAYAAJ'

        response = requests.get(url)

        if response.status_code != 200:
            self.stdout.write(self.style.ERROR('Ошибка при получении данных от API'))

        data = response.json()
        volume_info = data.get('volumeInfo')
        if not volume_info:
            self.stdout.write(self.style.WARNING('Нет данных о книге в ответе'))

        title = volume_info.get('title', 'Unknown Title')
        authors = volume_info.get('authors', ['Unknown Author'])
        published_date = volume_info.get('publishedDate', None)
        if published_date:
            try:
                published_date = datetime.datetime.strptime(published_date, '%Y-%m-%d')
            except ValueError:
                try:
                    published_date = datetime.datetime.strptime(published_date, '%Y-%m')
                    published_date = published_date.replace(day=1)
                except ValueError:
                    published_date = datetime.datetime.strptime(published_date, '%Y')
                    published_date = published_date.replace(month=1, day=1)
            published_date = published_date.date()
        # Создание или получение авторов
        author_objects = []
        for author_name in authors:
            first_name, last_name = author_name.split(' ', 1) if ' ' in author_name else (author_name, '')
            author, created = Author.objects.get_or_create(
                first_name=first_name,
                last_name=last_name
            )
            author_objects.append(author)

        # Создание и сохранение книги
        for author in author_objects:
            book = Book(
                author=author,
                title=title,
                published_date=published_date,
                is_available=True)
            book.save()

        self.stdout.write(self.style.SUCCESS(f'Успешно добавлена книга: {title}'))
