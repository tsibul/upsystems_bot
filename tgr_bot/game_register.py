import datetime
from datetime import timedelta
from game_management.models import Location, Schedule, Member, RegisteredToGame
from  backinfo import weekday_rus


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


def registered_text():
    today = datetime.date.today()
    i = 0
    return_text = 'Выберите даты, которые хотите посмотреть \n\n'
    while i < 7:
        curr_date = today + timedelta(days=i)
        number_registered = RegisteredToGame.objects.filter(schedule__date=curr_date, active=True).count()
        if number_registered != 0:
            return_text += weekday_rus(curr_date) + ', (' + curr_date.strftime('%d.%m.%Y') + '), ' + \
                           str(number_registered) + ' зарегистрировано\n'
        i += 1
    return return_text


def who_registered_persons(game_id):
    members = RegisteredToGame.objects.filter(schedule__id=game_id).values_list('member__nickname')
    persons_list = ''
    for pers in members:
        persons_list += pers[0] + '\n'
    return persons_list

def who_registered_images(game_id):
    games = RegisteredToGame.objects.filter(schedule__id=game_id)
    images_list = []
    for game in games:
        if game.member.photo_file.name is not None:
            images_list.append(game.member.photo_file)
    return images_list

