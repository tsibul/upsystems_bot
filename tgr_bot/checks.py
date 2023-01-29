import datetime

from game_management.models import Member, Lead, LeadLog
from backinfo import standard_commands as st
from promo import promo_text, price_text, discount_text, member_rating, master_rating
from schedule import schedule_date_game
from datetime import date, timezone

def hello_user(msg):
    lead_id = msg.id
    try:
        name = Member.objects.get(lead__tg_id=lead_id).nickname + ", рады новой встрече\! \n" \
                                                         "Чем хотите заняться?"
    except:
        name = Lead.objects.get(tg_id=lead_id).tg_name2 + "\!\n Первый раз здесь?\nЗалетай, регистрируйся \=\)\n" \
                              "Записывайся на игры и не забывай оставлять комментарии\."
    return name


def check_button(txt):
    ind = st.index(txt)
    if ind == 0:
        text = promo_text()
    elif ind == 1:
        text = master_rating()
    elif ind == 2:
        text = member_rating()
    elif ind == 3:
        text = schedule_date_game()
    elif ind == 4:
        text = price_text()
    elif ind == 5:
        text = discount_text()
    else:
        ...
        text = 'under construction'
    return text

def check_user(user):
    game_function = 'гость'
    try:
        lead = Lead.objects.get(tg_id=user.id)
        log_type = 'visit'
        try:
            member = Member.objects.get(lead=user)
            game_function = member.game_function.game_function
        except:
            member = None
    except:
        if user.username:
            name2 = user.username
        elif user.first_name and user.last_name:
            name2 = user.first_name + ' ' + user.last_name
        elif not user.first_name:
            name2 = user.last_name
        elif not user.last_name:
            name2 = user.first_name
        lead = Lead(tg_id=user.id, tg_name=user.username, tg_last_name=user.last_name,
                      tg_first_name=user.first_name, tg_name2=name2,
                      lead_date=date.today())
        lead.save()
        member = None
        log_type = 'lead'
    leadlog = LeadLog(lead=lead, date_time=datetime.datetime.now(timezone.utc), log_type=log_type, member=member)
    leadlog.save()
    return game_function

