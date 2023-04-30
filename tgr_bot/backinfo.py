from datetime import date, timedelta
from game_management.models import Schedule

standard_commands = [
    'О нас',
    'Рейтинг ведущих',
    'Рейтинг игроков',
    'Расписание',
    'Стоимость',
    'Скидки',
    'Кто записан',
]

phone_no_commands = [
    'Записаться на игру',
    'Отменить запись',
    'Оценить ведущих',
]

call_back_commands = [
    'Обратный звонок',
]

order_event_commands = [
    'Заказать мероприятие',
]

member_register_commands = [
    'Псевдоним',
    'Дата рождения',
    'Фото'
]

week_days = [
    'ПОНЕДЕЛЬНИК',
    'ВТОРНИК',
    'СРЕДА',
    'ЧЕТВЕРГ',
    'ПЯТНИЦА',
    'СУББОТА',
    'ВОСКРЕСЕНЬЕ'
]


def weekday_rus(date):
    if date.weekday() == 0:
        res = 'ПОНЕДЕЛЬНИК'
    elif date.weekday() == 1:
        res = 'ВТОРНИК'
    elif date.weekday() == 2:
        res = 'СРЕДА'
    elif date.weekday() == 3:
        res = 'ЧЕТВЕРГ'
    elif date.weekday() == 4:
        res = 'ПЯТНИЦА'
    elif date.weekday() == 5:
        res = 'СУББОТА'
    else:
        res = 'ВОСКРЕСЕНЬЕ'
    return res


def promo_relpace(txt):
    txt1 = txt.replace('.', '\.')
    txt2 = txt1.replace('-', '\-')
    txt3 = txt2.replace('/', '\/')
    txt4 = txt3.replace('_', '\_')
    return txt4


def date_loc_sch_dict():
    date_start = date.today()  # - timedelta(days=date.today().weekday())
    schedule = Schedule.objects.filter(date__gte=date_start, active=True, date__lte=(date_start + timedelta(days=6))). \
        order_by('date')
    sch_dict = {}
    for sch in schedule:
        if sch.date not in sch_dict:
            sch_dict[sch.date] = {}
        if sch.location not in sch_dict[sch.date]:
            sch_dict[sch.date][sch.location] = []
        sch_dict[sch.date][sch.location].append(sch)
    return sch_dict


def date_gam_sch_dict():
    date_start = date.today()  # - timedelta(days=date.today().weekday())
    schedule = Schedule.objects.filter(date__gte=date_start, active=True, date__lte=(date_start + timedelta(days=6))). \
        order_by('date')
    sch_dict = {}
    for sch in schedule:
        if sch.date not in sch_dict:
            sch_dict[sch.date] = {}
        if sch.game not in sch_dict[sch.date]:
            sch_dict[sch.date][sch.game] = []
        sch_dict[sch.date][sch.game].append(sch)
    return sch_dict
