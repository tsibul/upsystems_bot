**MySQL**

create db mafia

**Configure TelegramBot**

through BotFather as per Telegram manual

**Create directory**

/upsytems_bot

**in root create file config.cfg:**

[LOG_PAS]
user = 'user for DB'
pass = 'pass for DB'
sec_key = 'django security key'
[TG_BOT]
api = 'tg bot key'


**Git Pull** 

from https://github.com/tsibul/upsystems_bot.git

**Django**

pip install -r requirements.txt
python3 manage.py migrate

**RunServer**

python3 manage.py runserver :'port'

**Run bot**

tgr_bot.py with parameters

PYTHONUNBUFFERED=1;

DJANGO_SETTINGS_MODULE=upsystems_bot.settings 
