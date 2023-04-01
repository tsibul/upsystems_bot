import django
django.setup()


import telebot
import configparser

from locations import ret_address
from checks import hello_user, check_button, check_user, check_phone
from backinfo import standard_commands, phone_no_commands
from menu import show_buttons, give_number, member_register
from members import add_phone_no

config = configparser.RawConfigParser()
config.read('config.cfg')
config_dict = dict(config.items('TG_BOT'))
api = config_dict['api']

API_TOKEN = api

bot = telebot.TeleBot(API_TOKEN, num_threads=5)

bot.set_my_commands([
    telebot.types.BotCommand("/start", "запуск"),
    telebot.types.BotCommand("/help", "помощь"),
    telebot.types.BotCommand("/sign_in", "подписаться"),
    telebot.types.BotCommand("/register", "записаться на игру"),
    telebot.types.BotCommand("/schedule", "расписание"),
    telebot.types.BotCommand("/call", "обратный звонок"),
])


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    chat_id = message.from_user.id
    user_check = check_user(message.from_user)
    name = hello_user(message.from_user)
    bot.send_message(chat_id, "Привет, " + name, reply_markup=show_buttons(user_check), parse_mode='MarkdownV2')

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
#@bot.message_handler(func=lambda message)
#def


@bot.message_handler(content_types=['text'], func=lambda message: message.text in standard_commands)
def check_messages(message):
   chat_id = message.from_user.id
   bot.send_message(chat_id, check_button(message.text), parse_mode='MarkdownV2')


@bot.message_handler(content_types=['text'], func=lambda message: message.text == 'Отмена' or message.text == 'На главную')
def check_messages(message):
    chat_id = message.from_user.id
    user_check = check_user(message.from_user)
    bot.send_message(chat_id, '*Выберите пункт меню* \n ↓\t\t\t\t\t\t\t\t\t\t↓\t\t\t\t\t\t\t\t\t\t\t↓\t\t\t\t'
                              '\t\t\t\t\t\t\t↓', reply_markup=show_buttons(user_check), parse_mode='MarkdownV2')


@bot.message_handler(content_types=['text'], func=lambda message: message.text in phone_no_commands)
def check_messages(message):
   chat_id = message.from_user.id
   if check_phone(chat_id) == '':
       return bot.send_message(chat_id, text='Предоставить номер телефона', reply_markup=give_number(), parse_mode='MarkdownV2')
   bot.send_message(chat_id, 'записаться на игру')


@bot.message_handler(content_types=['contact'])
def check_messages(message):
    chat_id = message.from_user.id
    phone = message.contact.phone_number
    add_phone_no(chat_id, phone)
    bot.send_message(chat_id, '*Вы можете заполнить информацию о себе* \n ↓\t\t\t\t\t\t\t\t\t\t↓\t\t\t\t\t\t\t\t\t\t\t↓\t\t\t\t'
                              '\t\t\t\t\t\t\t↓', reply_markup=member_register(), parse_mode='MarkdownV2')





@bot.message_handler(func=lambda message: True)
def echo_message(message):
    chat_id = message.from_user.id
    if check_phone(chat_id) == '':
        give_number()
    bot.send_message(chat_id, ret_address())

def run():
    bot.infinity_polling()

run()