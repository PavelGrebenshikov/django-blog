from django.contrib import admin
from django.urls import path
from .views import PostsView, PostsDetail, PostsID

urlpatterns = [
    path('', PostsView.as_view()),
    path('home/', PostsView.as_view(), name="home_page"),
    path('home/<slug:slug>/', PostsDetail.as_view(), name='post_page'),
    path('home/post/<pk>/', PostsID.as_view(), name='post_number'),
]