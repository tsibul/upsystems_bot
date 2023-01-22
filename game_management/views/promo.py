from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required


@login_required()
def promo(request):
    context = {}
    return render(request, 'game_management/promo.html', context)
