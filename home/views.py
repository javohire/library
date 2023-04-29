from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from book.models import Book, Author, Category
from .serializers import BookSerializer, AuthorSerializer, CategorySerializer
from rest_framework import status



# Create your views here.

@api_view(['GET'])
def book_list(request):
    if request.method=='GET':
        books = Book.objects.all()

        serializer = BookSerializer(books, many=True)

        return Response(data=serializer.data)

@api_view(['GET'])
def single_book(request, slug):
    try:
        book = Book.objects.get(slug=slug)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer = BookSerializer(book)

        return Response(data=serializer.data)