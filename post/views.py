from django.db import models
from django.http.response import Http404
from django.shortcuts import redirect, render, get_object_or_404
from .models import Category, Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from banners.models import *


def is_valid_queryparam(param):
    return param != '' and param is not None



def last_posts(request):
    last_posts = Post.objects.all().order_by('-posting_date')
    contex = {
        'post': last_posts
    }
    return render(request, 'last_posts.html', contex)

def home_view(request):

    post = Post.objects.all()
    categories = Category.objects.all()
    last_posts = Post.objects.all().order_by('-posting_date')[:6]

    reklam = MainBanner.objects.all()
    cat = request.GET.get('category')
    banners = Banner.objects.all()


    query = request.GET.get('query')
    nov = request.GET.get('social')

    

    if is_valid_queryparam(cat):
        post = post.filter(category__title__icontains=cat)
        contex = {
            'post': post,
        }
        return render(request, 'query.html', contex)
    
    if is_valid_queryparam(query) and nov == 'Hamısı':
        post = post.filter(title__icontains=query)
        contex = {
            'post': post,
        }
        return render(request, 'query.html', contex)

    elif is_valid_queryparam(query) and nov != 'Hamısı':
        post = post.filter(title__icontains=query, linktype__icontains=nov)
        contex = {
            'post': post,
        }
        return render(request, 'query.html', contex)

    contex = {
        'categories': categories,
        'post': last_posts,
        
        'reklam': reklam,
        'banner': banners,
    }

    return render(request, 'index.html', contex)



@login_required(login_url='/account/login/')
def post_create(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

    contex = {
        'form': form,
    }

    return render(request, 'insert-book.html', contex)



def post_update(request, id):
    post = get_object_or_404(Post, id=id)

    if not request.user == post.user:
        raise Http404
    
    form = PostForm(request.POST or None, request.FILES or None, instance=post)

    if form.is_valid():
        form.save()

    contex = {
        'form': form,
    }

    return render(request, 'insert-book.html', contex)


def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    if not request.user == post.user:
         raise Http404
    post.delete()

    return redirect('home')






# Create your views here.
