import django
django.setup()

import telebot
import configparser
from locations import ret_address, ret_photo
from checks import hello_user, check_button
from menu import main_buttons
from telebot.types import Message, MenuButtonCommands
from backinfo import standard_commands

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
    name = hello_user(message.from_user)
    bot.send_message(chat_id, "Привет, " + name, reply_markup=main_buttons(), parse_mode='MarkdownV2')

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
#@bot.message_handler(func=lambda message)
#def


@bot.message_handler(content_types=['text'], func=lambda message: message.text in standard_commands)
def check_messages(message):
    chat_id = message.from_user.id
    bot.send_message(chat_id, check_button(message.text), parse_mode='MarkdownV2')


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    chat_id = message.from_user.id
    bot.send_message(chat_id, ret_address())

def run():
    bot.infinity_polling()

run()