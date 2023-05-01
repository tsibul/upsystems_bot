from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from game_management.models import Member


@login_required()
def members(request):
    members = Member.objects.all().order_by('registered_date')
    context = {'members': members}
    return render(request, 'game_management/members.html', context)
