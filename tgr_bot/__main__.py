import django
django.setup()

import telebot
import configparser
from locations import ret_address, ret_photo
from checks import hello_user
from menu import main_buttons
from telebot.types import Message

config = configparser.RawConfigParser()
config.read('config.cfg')
config_dict = dict(config.items('TG_BOT'))
api = config_dict['api']

API_TOKEN = api

bot = telebot.TeleBot(API_TOKEN, num_threads=5)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    chat_id = message.from_user.id
    name = hello_user(message.from_user)
    bot.send_message(chat_id, "Привет, " + name, reply_markup=main_buttons())

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
#@bot.message_handler(func=lambda message)
#def


@bot.message_handler(content_types=['text'], func=lambda message: message.text == 'О нас' or
                                                                  message.text == 'Обратный звонок'or
                                                                  message.text == 'Заказать мероприятие' or
                                                                  message.text == 'Расписание' or
                                                                  message.text == 'Стоимость' or
                                                                  message.text == 'Скидки' or
                                                                  message.text == 'Кто записан' or
                                                                  message.text == 'Записаться на игру' or
                                                                  message.text == 'Отменить запись'  or
                                                                  message.text == 'Оценить ведущих' or
                                                                  message.text == 'Рейтинг ведущих' or
                                                                  message.text == 'Рейтинг игроков')
def check_messages(message):
    chat_id = message.from_user.id
    bot.send_photo(chat_id, ret_photo())

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    chat_id = message.from_user.id
    bot.send_message(chat_id, ret_address())

def run():
    bot.infinity_polling()

run()