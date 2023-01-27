from game_management.models import Member

def hello_user(msg):
    member_id = msg.id
    try:
        name = Member.objects.get(tg_id=member_id).nickname + ", рады новой встрече! \n" \
                                                         "Чем хотите заняться?"
    except:
        name = str(msg.username) + "!\nПривет! Первый раз здесь?\nЗалетай, регистрируйся =)\n" \
                              "Записывайся на игры и не забывай оставлять комментарии."
    return name

