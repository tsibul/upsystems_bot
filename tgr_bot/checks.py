from game_management.models import Member
from backinfo import standard_commands as st
from promo import promo_text, price_text, discount_text
from schedule import schedule_text

def hello_user(msg):
    member_id = msg.id
    try:
        name = Member.objects.get(tg_id=member_id).nickname + ", рады новой встрече\! \n" \
                                                         "Чем хотите заняться?"
    except:
        name = str(msg.username) + "\!\n Первый раз здесь?\nЗалетай, регистрируйся \=\)\n" \
                              "Записывайся на игры и не забывай оставлять комментарии\."
    return name


def check_button(txt):
    ind = st.index(txt)
    if ind == 0:
        text = promo_text()
    elif ind == 3:
        text = schedule_text()
    elif ind == 4:
        text = price_text()
    elif ind == 5:
        text = discount_text()
    else:
        text = 'under construction'
    return text

