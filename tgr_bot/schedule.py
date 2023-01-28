from game_management.models import Schedule
import datetime
from datetime import date, timedelta
from backinfo import weekday_rus

def schedule_text():
    date_start = date.today() - timedelta(days=date.today().weekday())
    schedule = Schedule.objects.filter(date__gte=date_start, active=True, date__lte=(date_start + timedelta(days=6))).\
               order_by('date')
    text = ''
    for sch in schedule:
        text += '*' + sch.date.strftime('%d\.%m') + ' ' + weekday_rus(sch.date) + '*\n' + \
                sch.schedule_time_begin.strftime('%H:%M') + ' \- ' + sch.schedule_time_end.strftime('%H:%M') + '\. ' + \
                sch.game.game_name + '\. ' + sch.game.game_name + '\n' + \
                sch.location.location_name + '\. ' + sch.location.location_address + '\.\n\n'
    return text