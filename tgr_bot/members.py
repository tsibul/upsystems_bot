from game_management.models import Member, Lead, LeadLog, GameFunction
import datetime
from datetime import datetime


def add_phone_no(user_id, phone):
    lead = Lead.objects.get(tg_id=user_id)
    lead.phone_no = phone
    lead.save()
    try:
        member = Member.objects.get(lead=lead)
    except:
        game_function = GameFunction.objects.get(id=1)
        member = Member(lead=lead, nickname=lead.tg_name2, registered_date=datetime.today().date(),
                        game_function=game_function)
        member.save()


def update_nickname(message):
    message_id = message.from_user.id
    nickname = message.text
    member = Member.objects.get(lead__tg_id=message_id)
    member.nickname = nickname
    member.save()


def update_birthdate(message):
    message_id = message.from_user.id
    try:
        date_birth = datetime.strptime(message.text, '%d.%m.%Y')
        member = Member.objects.get(lead__tg_id=message_id)
        member.date_birth = date_birth
        member.save()
    except:
        pass


def update_photo_file(message):
    message_id = message.from_user.id
