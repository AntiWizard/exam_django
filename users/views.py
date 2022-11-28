from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.cache import *
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from users.forms import SignUpForm, LoginForm
from users.models import User


def signup(request):
    if request.user.is_anonymous:
        if request.method == "GET":
            signup_form = SignUpForm()
            return render(request, 'users/registrations/signup.html',
                          context={'form': signup_form})
        elif request.method == "POST":
            form = SignUpForm(request.POST)
            if not form.is_valid():
                messages.warning(
                    request,
                    "User with this Email address already!!"
                )
                return redirect('signup')
            if request.POST.get('password') != request.POST.get('password1'):
                messages.warning(
                    request,
                    "Password not same! Check again"
                )
                return redirect('signup')

        User.objects.create_user(username=request.POST.get('username'), password=request.POST.get('password'))
        messages.success(
            request,
            "You're register successfully!"
        )
        return redirect('login')
    else:
        return redirect('quiz_list')


def user_login(request):
    if request.user.is_anonymous:
        if request.method == "GET":
            cache.set('next', request.GET.get('next', None))

            login_form = LoginForm()
            return render(request, 'users/registrations/login.html', context={'form': login_form})
        elif request.method == "POST":
            user = authenticate(request, username=request.POST.get('username'),
                                password=request.POST.get('password'))
            if user is None:
                messages.warning(
                    request,
                    "User not Exist!!"
                )
                return redirect('login')
            login(request, user)
            next_url = cache.get('next')
            if next_url:
                cache.delete('next')
                return HttpResponseRedirect(next_url)
            return redirect('index')
    else:
        return redirect('index')


@login_required
def user_logout(request):
    logout(request)
    return redirect('index')
