from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required


def results(request):
    context = {}
    return render(request, 'game_management/results.html', context)
