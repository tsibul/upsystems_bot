import datetime
from game_management.models import Location, Schedule, Member, RegisteredToGame


def game_register(chat_id, register_type, location, game, date, time_begin, time_end):
    try:
        reg_location = Location.objects.get(location_name=location)
        reg_member = Member.objects.get(lead__tg_id=chat_id)
        reg_schedule = Schedule.objects.filter(game__game_name=game, date=date, schedule_time_begin=time_begin,
                                               schedule_time_end=time_end, location=reg_location).first()
    except:
        return False
    if register_type == 'checkout_game':
        game = RegisteredToGame.objects.get(member=reg_member, schedule=reg_schedule)
        game.active = False
        game.save()
    elif register_type == 'checkin_game':
        try:
            game = RegisteredToGame.objects.get(member=reg_member, schedule=reg_schedule)
        except:
            game = RegisteredToGame(member=reg_member, schedule=reg_schedule)
            game.save()
    else:
        return False
    return True
