from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required, permission_required
from game_management.views import tg_bot


@login_required()
def bot(request):
    context = {}
    return render(request, 'game_management/bot.html', context)
