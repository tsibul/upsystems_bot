from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from game_management.models import GameType, GameResult, Role, MemberResult, GameFunction, Location


@login_required()
def glossary(request):
    games = GameType.objects.all().count()
    game_results = GameResult.objects.all().count()
    roles = Role.objects.all().count()
    member_results = MemberResult.objects.all().count()
    game_functions = GameFunction.objects.all().count()
    locations = Location.objects.all().count()
    context = {'games': games, 'game_results': game_results, 'roles': roles, 'member_results': member_results,
               'game_functions': game_functions, 'locations': locations}
    return render(request, 'game_management/glossary.html', context)


@login_required()
def games(request):
    games = GameType.objects.all()
    context = {'games': games}
    return render(request, 'game_management/glossary/games.html', context)


def update_game(request):
    name = request.POST['name']
    description = request.POST['description']
    try:
        game_id = request.POST['game_id']
        game = GameType.objects.get(id=game_id)
        game.game_name = name
    except:
        game = GameType(game_name=name)
    game.game_description = description
    game.save()
    return HttpResponseRedirect(reverse('game_management:games'))


@login_required()
def game_result(request):
    results = GameResult.objects.all()
    game_types = GameType.objects.all()
    context = {'results': results, 'game_types': game_types}
    return render(request, 'game_management/glossary/game_result.html', context)


def update_result(request):
    name = request.POST['result']
    game = GameType.objects.get(id=request.POST['game'])
    try:
        result_id = request.POST['result_id']
        result = GameResult.objects.get(id=result_id)
        result.game_result = name
    except:
        result = GameResult(game_result=name)
    result.game_type = game
    result.save()
    return HttpResponseRedirect(reverse('game_management:game_result'))


@login_required()
def role(request):
    context = {}
    return render(request, 'game_management/glossary/role.html', context)


@login_required()
def member_result(request):
    context = {}
    return render(request, 'game_management/glossary/member_result.html', context)


@login_required()
def game_functions(request):
    context = {}
    return render(request, 'game_management/glossary/game_functions.html', context)


@login_required()
def location(request):
    context = {}
    return render(request, 'game_management/glossary/location.html', context)
