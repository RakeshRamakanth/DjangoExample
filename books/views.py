from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Books
from django.http import Http404

def index(request):
    all_books = Books.objects.all()
    context = {
        'all_books': all_books
    }
    return render(request,'books/index.html',context)

def detail(request, book_id):
    try:
        book = Books.objects.get(id=book_id)
    except Books.DoesNotExist:
        raise Http404('This page does not exists')
    context = {
        'book': book
    }
    return render(request,'books/detail.html',context)