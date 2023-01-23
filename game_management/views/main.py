from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User

from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import default_storage
from django.template import loader
from django.urls import reverse

#from .models import
from django.contrib.auth import authenticate, login
from game_management.forms import LoginForm
import datetime

# Create your views here.
@login_required()
def index(request):
    context = {}
    return render(request, 'game_management/index.html', context)
