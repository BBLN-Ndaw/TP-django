from django.urls import path
from .views import *
urlpatterns=[
    path("",index,name="index"), #pour une fonction, on ne met pas de .as_view()
    # [GeT, post books]+ [GET, PUT and DELETE]
    path("books",bookList.as_view(),name="book-list"),# as.view() car c'est une class
    path("books/<int:pk>",bookDetail.as_view(),name="book-details"),#car c'est une class
]