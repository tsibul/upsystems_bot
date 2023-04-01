# filters
#from tgr_bot.filters.admin_filter import AdminFilter

# handlers
#from handlers import send_welcome, echo_message
#from tgbot.handlers.admin import admin_user
#from tgbot.handlers.spam_command import anti_spam
#from tgbot.handlers.user import any_user

# middlewares
#from tgbot.middlewares.antiflood_middleware import antispam_func

# states
#from tgbot.states.register_state import Register

# utils
#from tgbot.utils.database import Database


# telebot
import telebot

from telebot import apihelper
apihelper.ENABLE_MIDDLEWARE = True

import configparser
config = configparser.RawConfigParser()
config.read('config.cfg')
config_dict = dict(config.items('TG_BOT'))
api = config_dict['api']

API_TOKEN = api

bot = telebot.TeleBot(API_TOKEN, num_threads=10)


def register_handlers():
    bot.register_message_handler(send_welcome, commands=['start', 'help'])
    bot.register_message_handler(echo_message, func=lambda message: True)

#    bot.register_message_handler(admin_user, commands=['start'], admin=True, pass_bot=True)
#    bot.register_message_handler(any_user, commands=['start'], admin=False, pass_bot=True)
#    bot.register_message_handler(anti_spam, commands=['spam'], pass_bot=True)

register_handlers()

# Middlewares
#bot.register_middleware_handler(antispam_func, update_types=['message'])


# custom filters
#bot.add_custom_filter(AdminFilter())

def run():
    bot.infinity_polling()


run()
