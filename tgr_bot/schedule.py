from backinfo import weekday_rus, promo_relpace, date_loc_sch_dict, date_gam_sch_dict


def schedule_date_location():
    sc = date_loc_sch_dict()
    text = ''
    for date in sc.keys():
        text += '\n*' + weekday_rus(date) + ' ' + date.strftime('%d.%m') + '*\n'
        for lc in sc[date].keys():
            text += '*' + lc.location_name + '.* ' + lc.location_address + \
                    '.\n' + lc.location_point + '\n'
            for game in sc[date][lc]:
                text += '*с ' + game.schedule_time_begin.strftime('%H:%M') + ' до ' + \
                        game.schedule_time_end.strftime('%H:%M') + '*\n' + \
                        game.game.game_name + '. ' + game.game.game_description + '\n'
    return promo_relpace(text)


def schedule_date_game():
    sc = date_gam_sch_dict()
    text = ''
    for date in sc.keys():
        text += '\n*' + weekday_rus(date) + ' ' + date.strftime('%d.%m') + '*\n'
        for game in sc[date].keys():
            text += 'Игры *' + game.game_name + '.* ' + game.game_description + '.\n'
            for sch in sc[date][game]:
                text += '*с ' + sch.schedule_time_begin.strftime('%H:%M') + ' до ' + \
                        sch.schedule_time_end.strftime('%H:%M') + '*\n' + \
                        sch.location.location_name + '. ' + sch.location.location_address + '\n' + \
                        sch.location.location_point + '\n'
    return promo_relpace(text)
