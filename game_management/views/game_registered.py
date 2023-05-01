import datetime
from datetime import timedelta

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from game_management.models import Member, RegisteredToGame, Schedule


@login_required()
def game_registered(request):
    today = datetime.date.today()
    schedule = Schedule.objects.filter(date__gte=today, date__lte=today + timedelta(days=6)).order_by('-date')
    registered_to_game = []
    for day in schedule:
        game = RegisteredToGame.objects.filter(schedule=day, active=True)
        number_registered = game.count()
        members = game.values_list('member__nickname', flat=True)
        registered_to_game.append([day, number_registered, members])
    context = {'registered_to_game': registered_to_game}
    return render(request, 'game_management/game_registered.html', context)

