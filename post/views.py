from django.db import models
from django.http.response import Http404, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import Category, Post, Like
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from banners.models import *
from django.contrib.auth.models import User
from django.db.models import  F


def is_valid_queryparam(param):
    return param != '' and param is not None


def top_50(request):
    post = Post.objects.all().order_by('like')[:50]
    categories = Category.objects.all()
    

    user = User.objects.all()
    reklam = MainBanner.objects.all()
    cat = request.GET.get('category')
    banners = Banner.objects.all()


    query = request.GET.get('query')
    # nov = request.GET.get('social')

    if is_valid_queryparam(cat):
        post = post.filter(category__title__icontains=cat)
        contex = {
            'post': post,
        }
        return render(request, 'query.html', contex)

    if is_valid_queryparam(query):
        post = post.filter(title__icontains=query)

        contex = {
            'post': post,
        }
        return render(request, 'query.html', contex)
    # if is_valid_queryparam(query) and nov == 'Hamısı':
    #     post = post.filter(title__icontains=query)
    #     contex = {
    #         'post': post,
    #     }
    #     return render(request, 'query.html', contex)

    # elif is_valid_queryparam(query) and nov != 'Hamısı':
    #     post = post.filter(title__icontains=query, linktype__icontains=nov)
    #     contex = {
    #         'post': post,
    #     }
    #     return render(request, 'query.html', contex)

    contex = {
        'categories': categories,
        'post': post,
        'user': user,
        'reklam': reklam,
        'banner': banners,
    }

    return render(request, 'top50.html', contex)



def last_posts(request):
    last_posts = Post.objects.all().order_by('-posting_date')
    

    contex = {
        'post': last_posts
    }
    return render(request, 'last_posts.html', contex)


def premium(request):
    premium = Post.objects.filter(preminium=True)
    
    contex = {
        'premium': premium,
    }

    return render(request, 'premium.html', contex)



def insta_posts(request):
    post = Post.objects.filter(linktype='Instagram')

    query = request.GET.get('query')

    cat = request.GET.get('category')
    categories = Category.objects.all()

    if is_valid_queryparam(cat):
        post = post.filter(category__title__icontains=cat)
        
        contex = {
            'post': post,
        }
        return render(request, 'query.html', contex)


    if is_valid_queryparam(query):
        post = post.filter(title__icontains=query)

        contex = {
            'post': post,
        }
        return render(request, 'query.html', contex)

    return render(request, 'insta_posts.html', {'post': post, 'categories': categories})    



def wp_posts(request):
    post = Post.objects.filter(linktype='Whatsapp')

    query = request.GET.get('query')

    cat = request.GET.get('category')
    categories = Category.objects.all()

    if is_valid_queryparam(cat):
        post = post.filter(category__title__icontains=cat)
        
        contex = {
            'post': post,
        }
        return render(request, 'query.html', contex)


    if is_valid_queryparam(query):
        post = post.filter(title__icontains=query)

        contex = {
            'post': post,
        }
        return render(request, 'query.html', contex)

    return render(request, 'telegram_posts.html', {'post': post, 'categories': categories})


def telegram_posts(request):
    post = Post.objects.filter(linktype='Telegram')

    query = request.GET.get('query')

    cat = request.GET.get('category')
    categories = Category.objects.all()

    if is_valid_queryparam(cat):
        post = post.filter(category__title__icontains=cat)
        
        contex = {
            'post': post,
        }
        return render(request, 'query.html', contex)


    if is_valid_queryparam(query):
        post = post.filter(title__icontains=query)

        contex = {
            'post': post,
        }
        return render(request, 'query.html', contex)

    return render(request, 'telegram_posts.html', {'post': post, 'categories': categories})





def youtube_posts(request):
    post = Post.objects.filter(linktype='Youtube')

    query = request.GET.get('query')

    cat = request.GET.get('category')
    categories = Category.objects.all()

    if is_valid_queryparam(cat):
        post = post.filter(category__title__icontains=cat)
        
        contex = {
            'post': post,
        }
        return render(request, 'query.html', contex)


    if is_valid_queryparam(query):
        post = post.filter(title__icontains=query)

        contex = {
            'post': post,
        }
        return render(request, 'query.html', contex)

    return render(request, 'youtube_posts.html', {'post': post, 'categories': categories})


def tiktok_posts(request):
    post = Post.objects.filter(linktype='TikTok')

    query = request.GET.get('query')

    cat = request.GET.get('category')
    categories = Category.objects.all()

    if is_valid_queryparam(cat):
        post = post.filter(category__title__icontains=cat)
        
        contex = {
            'post': post,
        }
        return render(request, 'query.html', contex)


    if is_valid_queryparam(query):
        post = post.filter(title__icontains=query)

        contex = {
            'post': post,
        }
        return render(request, 'query.html', contex)

    return render(request, 'tiktok_posts.html', {'post': post, 'categories': categories}) 


def facebook_posts(request):
    post = Post.objects.filter(linktype='Facebook')

    query = request.GET.get('query')

    cat = request.GET.get('category')
    categories = Category.objects.all()

    if is_valid_queryparam(cat):
        post = post.filter(category__title__icontains=cat)
        
        contex = {
            'post': post,
        }
        return render(request, 'query.html', contex)


    if is_valid_queryparam(query):
        post = post.filter(title__icontains=query)

        contex = {
            'post': post,
        }
        return render(request, 'query.html', contex)

    return render(request, 'facebook_posts.html', {'post': post, 'categories': categories}) 




def home_view(request):

    post = Post.objects.all()
    categories = Category.objects.all()
    last_posts = Post.objects.all().order_by('-posting_date')[:30]
    premium = Post.objects.filter(preminium=True).order_by('?')[:6]
    users = User.objects.all()
    reklam = MainBanner.objects.all()
    cat = request.GET.get('category')
    banners = Banner.objects.all()
    profile = None
    
    if request.user.is_authenticated:
        profile = User.objects.get(username=request.user)


    query = request.GET.get('query')
    tg = request.GET.get('telegram')
    wp = request.GET.get('whatsapp')
    fb = request.GET.get('facebook')
    ins = request.GET.get('instagram')
    you = request.GET.get('youtube')
    tik = request.GET.get('tiktok')
    # nov = request.GET.get('social')

    query_posts= dict()

    like_say = Like.objects.all()
    


    if is_valid_queryparam(cat):
        post = post.filter(category__title__icontains=cat)
        
        contex = {
            'post': post,
        }
        return render(request, 'query.html', contex)


    if is_valid_queryparam(query):
        post = Post.objects.filter(title__icontains=query)

        query_posts.update(post)
        
        contex = {
            'post': query_posts,
        }

        return render(request, 'query.html', contex)
  
        


        # if is_valid_queryparam(query):
        #     post = post.filter(title__icontains=query)
        # if fb == 'Facebook':
        #     a= post.filter(linktype=fb)

        # if ins == 'Instagram':
        #     post = post.filter(linktype=ins)

        # if tg == 'Telegram' :
        #     post |= Post.objects.filter(linktype=tg)
        # if wp == 'Whatsapp':
        #     post |= Post.objects.filter(linktype=wp)
            

        # if you == 'Youtube':
        #     post = post.filter(linktype=you)

        # if tik == 'TikTok':
        #     post = post.filter(linktype=tik)
        contex = {
            'post': post,
        }
        return render(request, 'query.html', contex)
    




    # if is_valid_queryparam(query) and nov == 'Hamısı':
    #     post = post.filter(title__icontains=query)
    #     contex = {
    #         'post': post,
    #     }
    #     return render(request, 'query.html', contex)

    # elif is_valid_queryparam(query) and nov != 'Hamısı':
    #     post = post.filter(title__icontains=query, linktype__icontains=nov)
    #     contex = {
    #         'post': post,
    #     }
    #     return render(request, 'query.html', contex)

    contex = {
        'categories': categories,
        'post': last_posts,
        'user': users,
        'reklam': reklam,
        'banner': banners,
        'premium': premium,
        'profile': profile,
        'like_say': like_say,
    }

    return render(request, 'index.html', contex)



@login_required
def like_unlike_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)
        profile = User.objects.get(username=user)

        if profile in post_obj.liked.all():
            post_obj.liked.remove(profile)
        else:
            post_obj.liked.add(profile)

        like, created = Like.objects.get_or_create(user=profile, post_id=post_id)

        if not created:
            if like.value=='Like':
                like.value='Unlike'
            else:
                like.value='Like'
        else:
            like.value='Like'

            post_obj.save()
            like.save()

        data = {
            'value': like.value,
            'likes': post_obj.liked.all().count()
        }

        return JsonResponse(data, safe=False)


    # return JsonResponse({'data': data}, status=200)

@login_required(login_url='/account/register/')
def post_create(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')

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
        return redirect('home')

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
