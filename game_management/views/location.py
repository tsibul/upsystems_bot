from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from game_management.models import GameType, GameResult, Role, MemberResult, GameFunction, Location
from django.contrib.auth.models import User

def location(request):
    locations = Location.objects.filter(active=True)
    context = {'locations': locations}
    return render(request, 'game_management/location.html', context)

def update_location(request):
    loc_name = request.POST['name']
    loc_address = request.POST['address']
    loc_direction = request.POST['direction']
    loc_point = request.POST['point']
    try:
        loc_scheme = request.FILES['scheme']
    except:
        loc_scheme = None
    try:
        loc_photo = request.FILES['photo']
    except:
        loc_photo = None
    try:
        loc_id = request.POST['loc_id']
        loc = Location.objects.get(id=loc_id)
        loc.location_name = loc_name
    except:
        loc = Location(location_name=loc_name)
    loc.location_address = loc_address
    loc.location_directions = loc_direction
    loc.location_point = loc_point
    loc.location_photo = loc_photo
    loc.direction_photo = loc_scheme
    loc.save()
    return HttpResponseRedirect(reverse('game_management:location'))


def delete_location(request):
    try:
        location = Location.objects.get(id=request.POST['to_delete'])
        location.active = False
        location.save()
    except:
        pass
    return HttpResponseRedirect(reverse('game_management:location'))
