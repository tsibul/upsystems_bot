from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from game_management.models import Member

@login_required()
def game_registered(request):
    context = {}
    return render(request, 'game_management/game_registered.html', context)