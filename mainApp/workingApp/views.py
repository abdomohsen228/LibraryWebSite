from django.shortcuts import render, get_object_or_404,redirect
from .models import *
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import JsonResponse

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
        'user': request.user
    }
    return render(request, 'pages/User_Home.html',context)


def template(request):
    return render(request, 'pages/template.html')

def userBookList(request):
    # Get the UserProfile of the logged-in user
    user_profile = UserProfile.objects.get(user=request.user)
    # Filter books associated with this user's profile
    books = user_profile.book_list.all()

    context = {
        'books': books,
    }
    return render(request, 'pages/userBookList.html', context)

def userBorrowBook(request):
    if request.method == 'POST':
        book_id = request.POST.get('borrow')
        if book_id:
            book = get_object_or_404(Book, id=book_id)
            user_profile = UserProfile.objects.get(user=request.user)
            if book not in user_profile.book_list.all():
                user_profile.book_list.add(book)
                user_profile.save()
                return redirect('userBookList')  
            else:
                context = {
                    'books': Book.objects.all(),
                    'error': 'You have already borrowed this book.'
                }
                return render(request, 'pages/userBorrowBook.html', context)
    else:
        context = {
            'books': Book.objects.all(),
        }
        return render(request, 'pages/userBorrowBook.html', context)

def userSearchBooks(request):
    query = request.GET.get('query', '')
    books = Book.objects.filter(
        Q(title__icontains=query) |
        Q(author__icontains=query) 
    ) if query else Book.objects.all()
    
    context = {
        'books': books,
        'query': query
    }
    return render(request, 'pages/userSearchBooks.html', context)

def ajax_search_books(request):
    query = request.GET.get('query', '')
    books = Book.objects.filter(
        Q(title__icontains=query) |
        Q(author__icontains=query) 
    ) if query else Book.objects.all()

    results = []
    for book in books:
        results.append({
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'details': book.details,
            'image': book.image.url  # Add the image URL
        })
    
    return JsonResponse({'books': results})


def template(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    context = {
        'book': book,
    }
    return render(request, 'pages/template.html', context)

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
