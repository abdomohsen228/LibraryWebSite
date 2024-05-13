from django.shortcuts import render
from .models import *

# Create your views here.
# user functions
def User_Home(request):
    context={
        'books': Book.objects.all(),
    }
    return render(request, 'pages/User_Home.html',context)


def template(request):
    return render(request, 'pages/template.html')

def userBookList(request):
    return render(request, 'pages/userBookList.html')

def userBorrowBook(request):
    return render(request, 'pages/userBorrowBook.html')

def userSearchBooks(request):
    context={
        'books': Book.objects.all(),
    }
    return render(request, 'pages/userSearchBooks.html',context)


def userViewList(request):
    return render(request, 'pages/userViewList.html')

# admin function
def adminAddBooks(request):
    return render(request, 'pages/adminAddBooks.html')

def adminDeleteBooks(request):
    return render(request, 'pages/adminDeleteBooks.html')


def adminEditBooks(request):
    return render(request, 'pages/adminEditBooks.html')
