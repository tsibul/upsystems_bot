from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from game_management.models import Schedule, Location, GameType
import datetime
from datetime import date, timedelta
from django.core.paginator import Paginator


@login_required()
def schedule(request):
    schedule_cur = Schedule.objects.filter(active=True).order_by('-date', 'schedule_time_begin')
    games = GameType.objects.filter(active=True).order_by('game_name')
    location = Location.objects.filter(active=True).order_by('location_name')
    date_start = date.today() - timedelta(days=date.today().weekday())
    schedule_dic = {}
    schedule_last = {}
    for sch in schedule_cur:
        if sch.date >= date_start:
            if sch.date not in schedule_last:
                schedule_last[sch.date] = []
            schedule_last[sch.date].append(sch)
        else:
            if sch.date not in schedule_dic:
                schedule_dic[sch.date] = []
            schedule_dic[sch.date].append(sch)

    paginator = Paginator(list(schedule_dic.items()), 21)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    schedule = dict(page_obj.object_list)


    context = {'schedule_last': schedule_last, 'date_start': date_start, 'page_obj': page_obj, 'games': games,
               'location': location, 'schedule': schedule}
    return render(request, 'game_management/schedule.html', context)


def schedule_update(request):
    date = request.POST['date']
    begin = request.POST['time_begin']
    end = request.POST['time_end']
    loc_id = request.POST['location']
    game_id = request.POST['game']
    location = Location.objects.get(id=loc_id)
    game = GameType.objects.get(id=game_id)
    try:
        sch_id = request.POST['sch_id']
        schedule = Schedule.objects.get(id=sch_id)
        schedule.date = date
    except:
        schedule = Schedule(date=date)
    schedule.schedule_time_begin = begin
    schedule.schedule_time_end = end
    schedule.location = location
    schedule.game = game
    schedule.save()
    return HttpResponseRedirect(reverse('game_management:schedule'))
