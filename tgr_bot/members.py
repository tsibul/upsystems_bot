from game_management.models import Member, Lead, LeadLog, GameFunction
import datetime


def add_phone_no(user_id, phone):
    lead = Lead.objects.get(tg_id=user_id)
    lead.phone_no = phone
    lead.save()
    try:
        member = Member.objects.get(lead=lead)
    except:
        game_function = GameFunction.objects.get(id=1)
        member = Member(lead=lead, nickname=lead.tg_name2, registered_date=datetime.date.today(),
                        game_function=game_function)
        member.save()
