from django.shortcuts import get_object_or_404, redirect, render, redirect, HttpResponse
from .models import *
from .forms import *
from .serializers import *
from rest_framework import viewsets
# Create your views here.


def list_books(request):
    books = Book.objects.all()
    return render(request, 'library/list_books.html', {'books': books})




def add_book(request):
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        book_description = request.POST.get('book_description')
        author_id = request.POST.get('author')
        categories_ids = request.POST.getlist('categories')
        author = Author.objects.get(id=author_id)
        new_book = Book(book_name=book_name,
                        book_description=book_description, author=author)
        new_book.save()
        new_book.categories.set(Category.objects.filter(id__in=categories_ids))
        return redirect('list_books')
    else:
        authors = Author.objects.all()
        categories = Category.objects.all()
        return render(request, 'library/add_book.html', {'authors': authors, 'categories': categories})


def update_book(request, id):
    book = Book.objects.get(id=id)
    authors = Author.objects.all()
    categories = Category.objects.all()

    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        book_description = request.POST.get('book_description')
        author_id = request.POST.get('author')
        categories_ids = request.POST.getlist('categories')

        author = Author.objects.get(id=author_id)
        book_categories = Category.objects.filter(id__in=categories_ids)

        book.book_name = book_name
        book.book_description = book_description
        book.author = author
        book.save()
        book.categories.set(book_categories)
        return redirect('list_books')

    context = {
        'book': book,
        'authors': authors,
        'categories': categories
    }
    return render(request, 'library/update_book.html', context)



def add_author(request):
    if request.method == 'POST':
        author_name = request.POST.get('author_name')
        new_author = Author(name=author_name)
        new_author.save()
        return redirect('add_book')
    return render(request, 'library/add_author.html')


def add_category(request):
    if request.method == 'POST':
        cat_name = request.POST.get('cat_name')
        new_category = Category(cat_name=cat_name)
        new_category.save()
        return redirect('add_book')
    return render(request, 'library/add_category.html')


def delete_book(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'library/delete_book.html', {'book': book})


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
