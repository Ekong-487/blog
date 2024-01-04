from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('all_posts/', views.allPosts, name="all_posts"),
    path('post/<str:pk>/', views.post, name="post"),
    path('create_post/', views.createPost, name="create_post"),
    path('search/', views.search_posts, name='search_posts'),
 ]