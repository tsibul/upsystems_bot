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
from game_management.models import Promo

# Create your views here.
def index(request):
    promo = Promo.objects.filter(active=True).order_by('-promo_date').last()
    context = {'promo': promo}
    return render(request, 'game_management/index.html', context)
