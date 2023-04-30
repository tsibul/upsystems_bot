import datetime
from datetime import timedelta

from telebot import types
from backinfo import weekday_rus
from game_management.models import Schedule, RegisteredToGame, Member


def show_buttons(type):
    if type == 'игрок':
        return player_buttons()
    elif type == 'гость':
        return guest_buttons()
    elif type == 'ведущий':
        return master_buttons()


def player_buttons():
    markup = types.ReplyKeyboardMarkup(row_width=3)
    about_us = types.KeyboardButton('О нас')
    call_back = types.KeyboardButton('Обратный звонок')
    order_event = types.KeyboardButton('Заказать мероприятие')
    schedule = types.KeyboardButton('Расписание')
    prices = types.KeyboardButton('Стоимость')
    discount = types.KeyboardButton('Скидки')
    who_registered = types.KeyboardButton('Кто записан')
    to_register = types.KeyboardButton('Записаться на игру')
    decline_register = types.KeyboardButton('Отменить запись')
    vote_masters = types.KeyboardButton('Оценить ведущих')
    masters_rating = types.KeyboardButton('Рейтинг ведущих')
    members_rating = types.KeyboardButton('Рейтинг игроков')
    markup.add(about_us, call_back, order_event, schedule, prices, discount, who_registered, to_register,
               decline_register, vote_masters, masters_rating, members_rating)
    return markup


def guest_buttons():
    markup = types.ReplyKeyboardMarkup(row_width=3)
    about_us = types.KeyboardButton('О нас')
    call_back = types.KeyboardButton('Обратный звонок')
    order_event = types.KeyboardButton('Заказать мероприятие')
    schedule = types.KeyboardButton('Расписание')
    prices = types.KeyboardButton('Стоимость')
    discount = types.KeyboardButton('Скидки')
    who_registered = types.KeyboardButton('Кто записан')
    to_register = types.KeyboardButton('Записаться на игру')
    decline_register = types.KeyboardButton('Отменить запись')
    vote_masters = types.KeyboardButton('Оценить ведущих')
    masters_rating = types.KeyboardButton('Рейтинг ведущих')
    members_rating = types.KeyboardButton('Рейтинг игроков')
    markup.add(about_us, call_back, order_event, schedule, prices, discount, who_registered, to_register,
               decline_register, vote_masters, masters_rating, members_rating)
    return markup


def master_buttons():
    markup = types.ReplyKeyboardMarkup(row_width=3)
    call_back = types.KeyboardButton('Обратный звонок')
    order_event = types.KeyboardButton('Заказать мероприятие')
    schedule = types.KeyboardButton('Расписание')
    who_registered = types.KeyboardButton('Кто записан')
    to_register = types.KeyboardButton('Записаться на игру')
    decline_register = types.KeyboardButton('Отменить запись')
    vote_masters = types.KeyboardButton('Оценить ведущих')
    masters_rating = types.KeyboardButton('Рейтинг ведущих')
    members_rating = types.KeyboardButton('Рейтинг игроков')
    markup.add(call_back, order_event, schedule, who_registered, to_register,
               decline_register, vote_masters, masters_rating, members_rating)
    return markup


def give_number():
    markup = types.ReplyKeyboardMarkup(row_width=1)
    give_phone = types.KeyboardButton('Предоставить номер телефона', request_contact=True)
    discard = types.KeyboardButton('Отмена')
    markup.add(give_phone, discard)
    return markup


def order_event():
    markup = types.ReplyKeyboardMarkup()
    animator = types.KeyboardButton('Выезд ведущего', request_contact=True)
    event_online = types.KeyboardButton('Мероприятие Online')
    play_in_club = types.KeyboardButton('Поиграть своей компанией в клубе', request_contact=True)
    call_back = types.KeyboardButton('Обратный звонок')
    discard = types.KeyboardButton('На главную')
    markup.row(animator, event_online)
    markup.row(play_in_club, call_back, discard)
    return markup


def member_register():
    markup = types.ReplyKeyboardMarkup()
    nickname = types.KeyboardButton('Псевдоним')
    photo = types.KeyboardButton('Фото')
    birth_date = types.KeyboardButton('Дата рождения')
    discard = types.KeyboardButton('Отмена')
    markup.row(nickname, photo, birth_date)
    markup.row(discard)
    return markup


def game_register_menu_date(lead_id, register_type):
    today = datetime.date.today()
    markup = types.ReplyKeyboardMarkup()
    if register_type == 'checkin_game':
        games_available = Schedule.objects.filter(date__gte=today, date__lte=today + timedelta(days=6)).values_list(
            'date', flat=True).distinct().order_by('date')
        for game in games_available:
            msg_text = weekday_rus(game) + ' ' + game.strftime('%d.%m.%Y') + ' ' + 'Записаться'
            markup.row(msg_text)
    elif register_type == 'checkout_game':
        games_registered = RegisteredToGame.objects.filter(member__lead__tg_id=lead_id, schedule__date__gte=today,
                                                           schedule__date__lte=today + timedelta(days=6)).values_list(
            'schedule__date', flat=True).distinct().order_by('schedule__date')
        for game in games_registered:
            msg_text = weekday_rus(game) + ' ' + game.strftime('%d.%m.%Y') + ' Записаться'
            markup.row(msg_text)
    elif register_type == 'master_rating':
        game_masters = Member.objects.filter(game_function__game_function='ведущий')
        for master in game_masters:
            markup.row(master + ' Оценить')
    markup.row('Отмена')
    return markup
