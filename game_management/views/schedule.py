from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def schedule(request):
    context = {}
    return render(request, 'game_management/schedule.html', context)
