from game_management.models import Location

def ret_photo():
    loc = Location.objects.get(id=1)
    return loc.location_photo


def ret_address():
    loc = Location.objects.get(id=1)
    return loc.location_address
