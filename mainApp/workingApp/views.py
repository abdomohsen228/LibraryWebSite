from django.shortcuts import render
from .models import *

# Create your views here.
# user functions
def User_Home(request):
    return render(request, 'pages/User_Home.html')


def template(request):
    return render(request, 'pages/template.html')

def userBookList(request):
    return render(request, 'pages/userBookList.html')

def userBorrowBook(request):
    return render(request, 'pages/userBorrowBook.html')

def userSearchBooks(request):
    return render(request, 'pages/userSearchBooks.html')


def userViewList(request):
    return render(request, 'pages/userViewList.html')

# admin function
def adminAddBooks(request):
    return render(request, 'pages/adminAddBooks.html')

def adminDeleteBooks(request):
    return render(request, 'pages/adminDeleteBooks.html')


def adminEditBooks(request):
    return render(request, 'pages/adminEditBooks.html')
