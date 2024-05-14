from django.shortcuts import render
from .models import *
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from .forms import *



# Create your views here.
# user functions
def user_signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('User_Home')  # Adjust the redirect as needed
    else:
        form = UserSignupForm()
    return render(request, 'pages/SignUp.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('User_Home')  # Redirect to a success page.
    else:
        form = LoginForm()
    return render(request, 'pages/login.html', {'form': form})

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
    context={
        'books': Book.objects.all(),
    }
    return render(request, 'pages/userViewList.html',context)

# admin function
def adminAddBooks(request):
    return render(request, 'pages/adminAddBooks.html')

def adminDeleteBooks(request):
    return render(request, 'pages/adminDeleteBooks.html')


def adminEditBooks(request):
    return render(request, 'pages/adminEditBooks.html')
