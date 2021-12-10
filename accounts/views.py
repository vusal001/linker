from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse
from  django.contrib.auth import logout
from django.contrib import messages
from accounts.forms import LoginForm, RegisterForm
from django.contrib.auth.models import User

from post.models import Post





def loginview(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))

    form = LoginForm(request.POST or None)
    if form.is_valid():
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['parol'])
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Daxil etdiyiniz şifrə və ya telefon nömrəsi yanlışdır. Zəhmət olmasa bir daha sınayın.')



    contex = {
        'form': form,
    }

    return render(request, 'sign-in.html', contex)



def registerview(request):
    # if request.user.is_authenticated:
    #     return HttpResponseRedirect(reverse('home'))
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        user= form.save(commit=False)
        password= form.cleaned_data.get('password1')
        user.set_password(password)
        user.save()
        new_user= authenticate(username=user.username, password=password, first_name=user.first_name)
        login(request, new_user)
        return redirect('home')

    contex = {
        'form': form,
    }

    return render(request, 'sign-up.html', contex)
    

def profil(request, username):
    user = get_object_or_404(User, username=username)


    if not request.user == user:
        raise Http404

    logged_in_user = request.user
    logged_in_user_posts = Post.objects.filter(user=user)

    contex={

        'post_list': logged_in_user_posts,
        'login': logged_in_user,

    }
    return render(request, 'accounts/profile.html', contex)


# Create your views here.
