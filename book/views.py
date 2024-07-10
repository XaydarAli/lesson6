from django.shortcuts import render
from .models import Book,Author
def home(request):
    return render(request,'home.html')
def books(request):
    books=Book.objects.all()
    context={'books':books}
    return render(request,'books.html',context)

def authors(request):
    authors=Author.objects.all()
    context={'authors':authors}
    return render(request,'authors.html',context)
