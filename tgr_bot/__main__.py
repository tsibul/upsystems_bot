import django

django.setup()

import telebot
import configparser

from locations import ret_address
from checks import hello_user, check_button, check_user, check_phone, check_ph_button
from backinfo import standard_commands, phone_no_commands, member_register_commands
from menu import show_buttons, give_number, member_register, game_register_menu_date
from members import add_phone_no, update_nickname, update_birthdate, update_photo_file
from game_register import *

config = configparser.RawConfigParser()
config.read('config.cfg')
config_dict = dict(config.items('TG_BOT'))
api = config_dict['api']

API_TOKEN = api

bot = telebot.TeleBot(API_TOKEN, num_threads=5)

bot.set_my_commands([
    telebot.types.BotCommand("/start", "запуск"),
    telebot.types.BotCommand("/help", "помощь"),
    telebot.types.BotCommand("/sign_in", "заполнить информацию о себе"),
    telebot.types.BotCommand("/register", "записаться на игру"),
    telebot.types.BotCommand("/schedule", "расписание"),
    telebot.types.BotCommand("/call", "обратный звонок"),
])


# Handle commands #######################

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    chat_id = message.from_user.id
    user_check = check_user(message.from_user)
    name = hello_user(message.from_user)
    bot.send_message(chat_id, "Привет, " + name, reply_markup=show_buttons(user_check), parse_mode='MarkdownV2')


@bot.message_handler(commands=['sign_in'])
def sign_in(message):
    chat_id = message.from_user.id
    if check_phone(chat_id) == '':
        return bot.send_message(chat_id, text='Предоставить номер телефона', reply_markup=give_number(),
                                parse_mode='MarkdownV2')
    bot.send_message(chat_id, '*Заполнить информацию о себе* \n ↓\t\t\t\t\t\t\t\t\t\t↓\t\t\t\t\t\t\t\t\t\t\t↓\t\t\t\t'
                              '\t\t\t\t\t\t\t↓', reply_markup=member_register(), parse_mode='MarkdownV2')


# Handle contacts ######################

@bot.message_handler(content_types=['contact'])
def check_messages_contact(message):
    chat_id = message.from_user.id
    phone = message.contact.phone_number
    add_phone_no(chat_id, phone)
    bot.send_message(chat_id,
                     '*Вы можете заполнить информацию о себе* \n ↓\t\t\t\t\t\t\t\t\t\t↓\t\t\t\t\t\t\t\t\t\t\t↓\t\t\t\t'
                     '\t\t\t\t\t\t\t↓', reply_markup=member_register(), parse_mode='MarkdownV2')


# Handle text #############################

@bot.message_handler(content_types=['text'], func=lambda message: message.text in standard_commands)
def check_messages_standard_commands(message):
    chat_id = message.from_user.id
    bot.send_message(chat_id, check_button(message.text), parse_mode='MarkdownV2')


@bot.message_handler(content_types=['text'],
                     func=lambda message: message.text == 'Отмена' or message.text == 'На главную')
def check_messages_main_discard(message):
    chat_id = message.from_user.id
    user_check = check_user(message.from_user)
    bot.send_message(chat_id, '*Выберите пункт меню* \n ↓\t\t\t\t\t\t\t\t\t\t↓\t\t\t\t\t\t\t\t\t\t\t↓\t\t\t\t'
                              '\t\t\t\t\t\t\t↓', reply_markup=show_buttons(user_check), parse_mode='MarkdownV2')


@bot.message_handler(content_types=['text'], func=lambda message: message.text in phone_no_commands)
def check_messages_phone_no_commands(message):
    chat_id = message.from_user.id
    if check_phone(chat_id) == '':
        return bot.send_message(chat_id, text='Предоставить номер телефона', reply_markup=give_number(),
                                parse_mode='MarkdownV2')
    register_type = check_ph_button(message.text)
    bot.send_message(chat_id, 'выберите', reply_markup=game_register_menu_date(chat_id, register_type))


@bot.message_handler(content_types=['text'], func=lambda message: message.text in member_register_commands)
def nickname_birth_photo(message):
    chat_id = message.from_user.id
    if message.text == 'Псевдоним':
        bot.send_message(chat_id, 'введите псевдоним')
        bot.register_next_step_handler(message, update_nick)
    elif message.text == 'Дата рождения':
        bot.send_message(chat_id, 'введите дату рождения в формате дд.мм.ГГГГ')
        bot.register_next_step_handler(message, update_birth)
    else:
        bot.send_message(chat_id, 'загрузите фото')
        bot.register_next_step_handler(message, update_photo)


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    chat_id = message.from_user.id
    if check_phone(chat_id) == '':
        give_number()
    bot.send_message(chat_id, ret_address())


# Handle next message #####################################

def update_nick(message):
    chat_id = message.from_user.id
    update_nickname(message)
    bot.send_message(chat_id,
                     '↓\t\t\t\t\t\t\t\t\t\t↓\t\t\t\t\t\t\t\t\t\t\t↓\t\t\t\t'
                     '\t\t\t\t\t\t\t↓', reply_markup=member_register(), parse_mode='MarkdownV2')


def update_birth(message):
    chat_id = message.from_user.id
    update_birthdate(message)
    bot.send_message(chat_id,
                     '↓\t\t\t\t\t\t\t\t\t\t↓\t\t\t\t\t\t\t\t\t\t\t↓\t\t\t\t'
                     '\t\t\t\t\t\t\t↓', reply_markup=member_register(), parse_mode='MarkdownV2')


def update_photo(message):
    chat_id = message.from_user.id
    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    update_photo_file(chat_id, downloaded_file)
    bot.send_message(chat_id,
                     '↓\t\t\t\t\t\t\t\t\t\t↓\t\t\t\t\t\t\t\t\t\t\t↓\t\t\t\t'
                     '\t\t\t\t\t\t\t↓', reply_markup=member_register(), parse_mode='MarkdownV2')


#####################


def run():
    bot.infinity_polling()


run()
