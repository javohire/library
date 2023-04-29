from django.urls import path

from .views import book_list, single_book

urlpatterns = [
    path('', book_list, name='book_list'),
    path('book/<slug:slug>', single_book, name='single_book')
]
