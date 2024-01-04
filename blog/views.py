from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import PostForm

# Create your views here.
def home(request):
    recent_posts = Post.objects.order_by('-timestamp')[:5]

    return render(request, 'blog/home.html', {'recent_posts': recent_posts})

def post(request, pk):
    blogpost = Post.objects.get(id=pk)
    context = {'blogpost': blogpost}

    return render(request, 'blog/post.html', context)

def createPost(request):

    form = PostForm()
    if request.method == 'POST':
        form=PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'blog/create_post.html', context) 

def allPosts(request):
    posts = Post.objects.all()

    context = {'posts' : posts}
    return render(request, 'blog/all_posts.html', context)

def search_posts(request):
    query = request.GET.get('query')  # Get the user's query from the form
    if query:
        # Search for posts that contain the query in their title or content
        posts = Post.objects.filter(title__icontains=query) | Post.objects.filter(content__icontains=query)
    else:
        # If no query provided, return all posts (or handle it as you prefer)
        posts = Post.objects.all()

    return render(request, 'blog/all_posts.html', {'posts': posts})

