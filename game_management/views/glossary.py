from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from game_management.models import GameType, GameResult, Role, MemberResult, GameFunction, Location


@login_required()
def glossary(request):
    games = GameType.objects.filter(active=True).count()
    game_results = GameResult.objects.filter(active=True).count()
    roles = Role.objects.filter(active=True).count()
    member_results = MemberResult.objects.filter(active=True).count()
    game_functions = GameFunction.objects.filter(active=True).count()
    locations = Location.objects.filter(active=True).count()
    context = {'games': games, 'game_results': game_results, 'roles': roles, 'member_results': member_results,
               'game_functions': game_functions, 'locations': locations}
    return render(request, 'game_management/glossary.html', context)


@login_required()
def games(request):
    games = GameType.objects.filter(active=True)
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


def delete_game(request):
    try:
        game = GameType.objects.get(id=request.POST['to_delete'])
        game.active = False
        game.save()
    except:
        pass
    return HttpResponseRedirect(reverse('game_management:games'))


@login_required()
def game_result(request):
    results = GameResult.objects.filter(active=True)
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


def delete_result(request):
    try:
        result = GameResult.objects.get(id=request.POST['to_delete'])
        result.active = False
        result.save()
    except:
        pass
    return HttpResponseRedirect(reverse('game_management:game_result'))

@login_required()
def role(request):
    roles = Role.objects.filter(active=True)
    game_types = GameType.objects.filter(active=True)
    context = {'roles': roles, 'game_types': game_types}
    return render(request, 'game_management/glossary/role.html', context)


def update_role(request):
    role_name = request.POST['role']
    description = request.POST['description']
    side = request.POST['side']
    game = GameType.objects.get(id=request.POST['game'])
    try:
        role_id = request.POST['role_id']
        role = Role.objects.get(id=role_id)
        role.role = role_name
    except:
        role = Role(role=role_name)
    role.role_description = description
    role.side = side
    role.game = game
    role.save()
    return HttpResponseRedirect(reverse('game_management:role'))


def delete_role(request):
    try:
        role = Role.objects.get(id=request.POST['to_delete'])
        role.active = False
        role.save()
    except:
        pass
    return HttpResponseRedirect(reverse('game_management:role'))


@login_required()
def member_result(request):
    results = MemberResult.objects.filter(active=True)
    context = {'results': results}
    return render(request, 'game_management/glossary/member_result.html', context)


def update_member_result(request):
    result = request.POST['name']
    result_type = request.POST['description']
    try:
        result_id = request.POST['game_id']
        member_result = MemberResult.objects.get(id=result_id)
        member_result.member_result = result
    except:
        member_result = MemberResult(member_result=result)
    member_result.member_result_type = result_type
    member_result.save()
    return HttpResponseRedirect(reverse('game_management:member_result'))


def delete_member_result(request):
    try:
        member_result = MemberResult.objects.get(id=request.POST['to_delete'])
        member_result.active = False
        member_result.save()
    except:
        pass
    return HttpResponseRedirect(reverse('game_management:member_result'))

@login_required()
def game_functions(request):
    game_function = GameFunction.objects.filter(active=True)
    context = {'game_function': game_function}
    return render(request, 'game_management/glossary/game_functions.html', context)


def update_function(request):
    name = request.POST['name']
    description = request.POST['description']
    try:
        game_id = request.POST['game_id']
        function = GameFunction.objects.get(id=game_id)
        function.game_function = name
    except:
        function = GameFunction(game_function=name)
    function.game_function_description = description
    function.save()
    return HttpResponseRedirect(reverse('game_management:game_functions'))


def delete_function(request):
    try:
        game = GameFunction.objects.get(id=request.POST['to_delete'])
        game.active = False
        game.save()
    except:
        pass
    return HttpResponseRedirect(reverse('game_management:game_functions'))


@login_required()
def location(request):
    context = {}
    return render(request, 'game_management/glossary/location.html', context)
