from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required


@login_required()
def members(request):
    context = {}
    return render(request, 'game_management/members.html', context)
