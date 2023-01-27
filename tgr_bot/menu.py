import telebot
from telebot import types


def main_buttons():
    markup = types.ReplyKeyboardMarkup(row_width=3)
    about_us = types.KeyboardButton('О нас')
    call_back = types.KeyboardButton('Обратный звонок')
    order_event = types.KeyboardButton('Заказать мероприятие')
    schedule = types.KeyboardButton( 'Расписание')
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
