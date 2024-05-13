from django.urls import path
from . import views

urlpatterns=[
    path('User_Home/',views.User_Home,name='User_Home'),
    path('template/',views.template,name='template'),
    path('userBookList/',views.userBookList,name='userBookList'),
    path('userBorrowBook/',views.userBorrowBook,name='userBorrowBook'),
    path('userSearchBooks/',views.userSearchBooks,name='userSearchBooks'),
    path('userViewList/',views.userViewList,name='userViewList'),
    path('adminAddBooks/',views.adminAddBooks,name='adminAddBooks'),
    path('adminDeleteBooks/',views.adminDeleteBooks,name='adminDeleteBooks'),
    path('adminEditBooks/',views.adminEditBooks,name='adminEditBooks'),

]
