from game_management.models import Promo
from backinfo import promo_relpace

def promo_text():
    promo = Promo.objects.filter(active=True, promo_type='О нас').order_by('-promo_date').first()
    promo_txt = '\t' + promo.par1 + '\t' + promo.text1 + '\n\n' + \
                '\t' + promo.par2 + '\t' + promo.text2 + '\n\n' + \
                '\t' + promo.par3 + '\t' + promo.text3 + '\n\n' + \
                '\t' + promo.par4 + '\t' + promo.text4
    return promo_relpace(promo_txt)


def price_text():
    promo = Promo.objects.filter(active=True, promo_type='Цены').order_by('-promo_date').first()
    price_txt = '\t' + promo.par1 + '\t' + promo.text1 + '\n\n' + \
                '\t' + promo.par2 + '\t' + promo.text2 + '\n\n' + \
                '\t' + promo.par3 + '\t' + promo.text3 + '\n\n' + \
                '\t' + promo.par4 + '\t' + promo.text4
    return promo_relpace(price_txt)


def discount_text():
    promo = Promo.objects.filter(active=True, promo_type='Скидки').order_by('-promo_date').first()
    discount_txt = '\t' + promo.par1 + '\t' + promo.text1 + '\n\n' + \
                '\t' + promo.par2 + '\t' + promo.text2 + '\n\n' + \
                '\t' + promo.par3 + '\t' + promo.text3 + '\n\n' + \
                '\t' + promo.par4 + '\t' + promo.text4

    return promo_relpace(discount_txt)


def member_rating():
    promo = Promo.objects.filter(active=True, promo_type='Рейтинг игроков').order_by('-promo_date').first()
    member_txt = '\t' + promo.par1 + '\t' + promo.text1 + '\n\n' + \
                '\t' + promo.par2 + '\t' + promo.text2 + '\n\n' + \
                '\t' + promo.par3 + '\t' + promo.text3 + '\n\n' + \
                '\t' + promo.par4 + '\t' + promo.text4

    return promo_relpace(member_txt)


def master_rating():
    promo = Promo.objects.filter(active=True, promo_type='Рейтинг ведущих').order_by('-promo_date').first()
    master_txt = '\t' + promo.par1 + '\t' + promo.text1 + '\n\n' + \
                '\t' + promo.par2 + '\t' + promo.text2 + '\n\n' + \
                '\t' + promo.par3 + '\t' + promo.text3 + '\n\n' + \
                '\t' + promo.par4 + '\t' + promo.text4

    return promo_relpace(master_txt)