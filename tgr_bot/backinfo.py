from datetime import datetime
standard_commands = [
                     'О нас',
                     'Рейтинг ведущих',
                     'Рейтинг игроков',
                     'Расписание',
                     'Стоимость',
                     'Скидки',
                     'Кто записан',
                     'Записаться на игру',
                     'Отменить запись',
                     'Оценить ведущих',
                     'Обратный звонок',
                     'Заказать мероприятие',
                     ]

def weekday_rus(date):
    if date.weekday() == 0:
        res = 'Понедельник'
    elif date.weekday() == 1:
        res = 'Вторник'
    elif date.weekday() == 2:
        res = 'Среда'
    elif date.weekday() == 3:
        res = 'Четверг'
    elif date.weekday() == 4:
        res = 'Пятница'
    elif date.weekday() == 5:
        res = 'Суббота'
    else:
        res = 'Воскресенье'
    return res