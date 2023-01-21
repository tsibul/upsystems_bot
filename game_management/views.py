from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User

from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import default_storage
from django.template import loader
from django.urls import reverse

#from .models import
from django.contrib.auth import authenticate, login
from .forms import LoginForm
import datetime

# Create your views here.
@login_required()
def index(request):
    context = {}
    return render(request, 'game_management/main.html', context)


@login_required()
def schedule(request):
    context = {}
    return render(request, 'game_management/schedule.html', context)


@login_required()
def members(request):
    context = {}
    return render(request, 'game_management/members.html', context)


@login_required()
def masters(request):
    context = {}
    return render(request, 'game_management/masters.html', context)


@login_required()
def results(request):
    context = {}
    return render(request, 'game_management/results.html', context)


@login_required()
def rating(request):
    context = {}
    return render(request, 'game_management/rating.html', context)


@login_required()
def promo(request):
    context = {}
    return render(request, 'game_management/promo.html', context)


@login_required()
def bot(request):
    context = {}
    return render(request, 'game_management/bot.html', context)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})
