from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index, name= 'index'),
    #/books/1
    url(r'^(?P<book_id>[0-9]+)/$',views.detail, name= 'detail'),
]