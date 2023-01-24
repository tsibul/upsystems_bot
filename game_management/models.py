from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from auditlog.registry import auditlog


fs_members = FileSystemStorage(location='files/members')
fs_promo = FileSystemStorage(location='files/promo')
fs_locations = FileSystemStorage(location='files/locations')
fs_directions = FileSystemStorage(location='files/directions')


class GameFunction (models.Model):
    """ function in game """
    game_function = models.CharField(max_length=40)
    game_function_description = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

    def __repr__(self):
        return self.game_function_description

    def __str__(self):
        return self.game_function


"""
    create_time = models.DateTimeField(auto_now=True)
    create_user = models.ForeignKey(User, models.SET_NULL, null=True, related_name='func_creator')
    update_time = models.DateTimeField(blank=True, null=True, default='',)
    update_user = models.ForeignKey(User, models.SET_NULL, null=True, related_name='func_editor')
    delete_time = models.DateTimeField(blank=True, null=True, default='')
    delete_user = models.ForeignKey(User, models.SET_NULL, null=True, related_name='func_destroyer')
"""



class GameType (models.Model):
    """ game types with description """
    game_name = models.CharField(max_length=100)
    game_description = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

    def __repr__(self):
        return self.game_name

    def __str__(self):
        return self.game_name


"""    
    create_time = models.DateTimeField(auto_now=True)
    create_user = models.ForeignKey(User, models.SET_NULL, null=True, related_name='type_creator')
    update_time = models.DateTimeField(blank=True, null=True, default='',)
    update_user = models.ForeignKey(User, models.SET_NULL, null=True, related_name='type_editor')
    delete_time = models.DateTimeField(blank=True, null=True, default='')
    delete_user = models.ForeignKey(User, models.SET_NULL, null=True, related_name='type_destroyer')
"""


class Role (models.Model):
    """ roles in game """
    role = models.CharField(max_length=40)
    role_description = models.CharField(max_length=255)
    side = models.CharField(max_length=100, default='')
    game = models.ForeignKey(GameType, models.SET_NULL, null=True)
    active = models.BooleanField(default=True)

    def __repr__(self):
        return self.role + ' ' + self.role_description

    def __str__(self):
        return self.role


"""
    create_time = models.DateTimeField(auto_now=True)
    create_user = models.ForeignKey(User, models.SET_NULL, null=True, related_name='role_creator')
    update_time = models.DateTimeField(blank=True, null=True, default='',)
    update_user = models.ForeignKey(User, models.SET_NULL, null=True, related_name='role_editor')
    delete_time = models.DateTimeField(blank=True, null=True, default='')
    delete_user = models.ForeignKey(User, models.SET_NULL, null=True, related_name='role_destroyer')
"""


class GameResult (models.Model):
    """ game result """
    game_type = models.ForeignKey(GameType, models.SET_NULL, null=True)
    game_result = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __repr__(self):
        return self.game_result

    def __str__(self):
        return self.game_result

'''
    create_time = models.DateTimeField(auto_now=True)
    create_user = models.ForeignKey(User, models.SET_NULL, null=True, related_name='game_result_creator')
    update_time = models.DateTimeField(blank=True, null=True, default='',)
    update_user = models.ForeignKey(User, models.SET_NULL, null=True, related_name='game_result_editor')
    delete_time = models.DateTimeField(blank=True, null=True, default='')
    delete_user = models.ForeignKey(User, models.SET_NULL, null=True, related_name='game_result_destroyer')
'''


class MemberResult (models.Model):
    member_result = models.CharField(max_length=100)
    member_result_type = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __repr__(self):
        return self.member_result

    def __str__(self):
        return self.member_result


'''
    create_time = models.DateTimeField(auto_now=True)
    create_user = models.ForeignKey(User, models.SET_NULL, null=True, related_name='member_result_creator')
    update_time = models.DateTimeField(blank=True, null=True, default='',)
    update_user = models.ForeignKey(User, models.SET_NULL, null=True, related_name='member_result_editor')
    delete_time = models.DateTimeField(blank=True, null=True, default='')
    delete_user = models.ForeignKey(User, models.SET_NULL, null=True, related_name='member_result_destroyer')
'''


class Member (models.Model):
    """ Club members table """
    tg_id = models.IntegerField(default=0)
    tg_name = models.CharField(max_length=255)
    date_birth = models.DateField(default='', blank=True, null=True)
    nickname = models.CharField(max_length=255, default='', null=True, blank=True)
    photo = models.BooleanField(default=False)
    photo_file = models.FileField(storage=fs_members, null=True, blank=True)
    game_function = models.ForeignKey(GameFunction, models.SET_NULL, null=True)
    active = models.BooleanField(default=True)

    def __repr__(self):
        return self.tg_name + ' '+ self.nickname

    def __str__(self):
        return self.nickname


'''
    create_time = models.DateTimeField(auto_now=True)
    create_user = models.ForeignKey(User, models.SET_NULL, null=True, related_name='member_creator')
    update_time = models.DateTimeField(blank=True, null=True, default='',)
    update_user = models.ForeignKey(User, models.SET_NULL, null=True, related_name='member_editor')
    delete_time = models.DateTimeField(blank=True, null=True, default='')
    delete_user = models.ForeignKey(User, models.SET_NULL, null=True, related_name='member_destroyer')
'''


class Location(models.Model):
    """ Locations table (point for Google Maps) """
    location_name = models.CharField(max_length=100)
    location_address = models.CharField(max_length=255)
    location_directions = models.CharField(max_length=255)
    location_point = models.CharField(max_length=255)
    location_photo = models.FileField(storage=fs_locations, null=True, blank=True)
    direction_photo = models.FileField(storage=fs_directions, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __repr__(self):
        return self.location_name

    def __str__(self):
        return self.location_name


'''
    create_time = models.DateTimeField(auto_now=True)
    create_user = models.ForeignKey(User, models.SET_NULL, null=True, related_name='location_creator')
    update_time = models.DateTimeField(blank=True, null=True, default='',)
    update_user = models.ForeignKey(User, models.SET_NULL, null=True, related_name='location_editor')
    delete_time = models.DateTimeField(blank=True, null=True, default='')
    delete_user = models.ForeignKey(User, models.SET_NULL, null=True, related_name='location_destroyer')
'''


class Schedule (models.Model):
    """ scedule only for each GameType, each Day, each Location """
    date = models.DateField(auto_now=False)
    schedule_time_begin = models.TimeField(auto_now=False)
    schedule_time_end = models.TimeField(auto_now=False)
    game = models.ForeignKey(GameType, models.SET_NULL, null=True)
    game_name = models.CharField(max_length=255)
    location = models.ForeignKey(Location, models.SET_NULL, null=True)
    location_name = models.CharField(max_length=140)
    active = models.BooleanField(default=True)

    def __repr__(self):
        return str(self.date) + ' ' + str(self.schedule_time_begin) + ' ' + self.game.game_name

    def __str__(self):
        return str(self.date) + ' ' + str(self.schedule_time_begin) + ' ' + self.game.game_name


'''
    create_time = models.DateTimeField(auto_now=True)
    create_user = models.ForeignKey(User, models.SET_NULL, null=True, related_name='schedule_creator')
    update_time = models.DateTimeField(blank=True, null=True, default='',)
    update_user = models.ForeignKey(User, models.SET_NULL, null=True, related_name='schedule_editor')
    delete_time = models.DateTimeField(blank=True, null=True, default='')
    delete_user = models.ForeignKey(User, models.SET_NULL, null=True, related_name='schedule_destroyer')
'''



class RegisteredToGame (models.Model):
    """ registered to the game """
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

    def __repr__(self):
        return str(self.schedule.date) + self.member.nickname

    def __str__(self):
        return str(self.schedule.date) + self.member.nickname


'''
    create_time = models.DateTimeField(auto_now=True)
    create_user = models.ForeignKey(User, models.SET_NULL, null=True, related_name='register_creator')
    update_time = models.DateTimeField(blank=True, null=True, default='',)
    update_user = models.ForeignKey(User, models.SET_NULL, null=True, related_name='register_editor')
    delete_time = models.DateTimeField(blank=True, null=True, default='')
    delete_user = models.ForeignKey(User, models.SET_NULL, null=True, related_name='register_destroyer')
'''


class GameInSchedule (models.Model):
    """ certain game with game master, time period & result"""
    schedule = models.ForeignKey(Schedule, models.SET_NULL, null=True)
    game_type = models.ForeignKey(GameType, models.SET_NULL, null=True)
    game_type_name = models.CharField(max_length=100)
    master = models.ForeignKey(Member, models.SET_NULL, null=True)
    master_nickname = models.CharField(max_length=255)
    time_begin = models.TimeField(auto_now=True)
    time_end = models.TimeField(auto_now=False)
    game_result = models.ForeignKey(GameResult, models.SET_NULL, null=True)
    active = models.BooleanField(default=True)

    def __repr__(self):
        return str(self.time_begin) + ' ' + self.game_type.game_name + ' ' + self.master.nickname

    def __str__(self):
        return str(self.time_begin) + ' ' + self.game_type.game_name + ' ' + self.master.nickname


'''
    create_time = models.DateTimeField(auto_now=True)
    create_user = models.ForeignKey(User, models.SET_NULL, null=True, related_name='game_creator')
    update_time = models.DateTimeField(blank=True, null=True, default='',)
    update_user = models.ForeignKey(User, models.SET_NULL, null=True, related_name='game_editor')
    delete_time = models.DateTimeField(blank=True, null=True, default='')
    delete_user = models.ForeignKey(User, models.SET_NULL, null=True, related_name='game_destroyer')
'''


class MemberInGame(models.Model):
    """ member results for the certain game"""
    game_in_schedule = models.ForeignKey(GameInSchedule, models.SET_NULL, null=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, models.SET_NULL, null=True)
    member_result_main = models.ForeignKey(MemberResult, models.SET_NULL, null=True, related_name='main_result')
    member_result_additional = models.ForeignKey(MemberResult, models.SET_NULL, null=True, related_name='additional_result')
    active = models.BooleanField(default=True)

    def __repr__(self):
        return str(self.game_in_schedule) + ' ' + self.member.nickname

    def __str__(self):
        return str(self.game_in_schedule) + ' ' + self.member.nickname


'''
    create_time = models.DateTimeField(auto_now=True)
    create_user = models.ForeignKey(User, models.SET_NULL, null=True, related_name='member_in_game_creator')
    update_time = models.DateTimeField(blank=True, null=True, default='',)
    update_user = models.ForeignKey(User, models.SET_NULL, null=True, related_name='member_in_game_editor')
    delete_time = models.DateTimeField(blank=True, null=True, default='')
    delete_user = models.ForeignKey(User, models.SET_NULL, null=True, related_name='member_in_game_destroyer')
'''


class MemberRating (models.Model):
    """ member rating for period ending rating date"""
    rating_date = models.DateField()
    game = models.ForeignKey(GameType, models.SET_NULL, null=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __repr__(self):
        return self.member.nickname + ' ' + str(self.rating)

    def __str__(self):
        return self.member.nickname + ' ' + str(self.rating)


class MemberStatistics (models.Model):
    """ member statistics for period ending statistic_date"""
    statistic_date = models.DateField()
    game = models.ForeignKey(GameType, models.SET_NULL, null=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, models.SET_NULL, null=True)
    result = models.ForeignKey(MemberResult, models.SET_NULL, null=True)

    def __repr__(self):
        return str(self.statistic_date) + ' ' + self.game.game_name + ' ' + self.member.nickname + ' ' + self.role.role + ' ' + self.result.member_result

    def __str__(self):
        return str(self.statistic_date) + ' ' + self.game.game_name + ' ' + self.member.nickname + ' ' + self.role.role + ' ' + self.result.member_result


class Promo (models.Model):
    """ text for promo devided in 4 parts par — emojy before each part"""
    promo_date = models.DateField
    par1 = models.CharField(max_length=10)
    text1 = models.CharField(max_length=400)
    par2 = models.CharField(max_length=10)
    text2 = models.CharField(max_length=400)
    par3 = models.CharField(max_length=10)
    text3 = models.CharField(max_length=400)
    par4 = models.CharField(max_length=10)
    text4 = models.CharField(max_length=400)
    active = models.BooleanField(default=True)

    def __repr__(self):
        return 'promo ' + str(self.promo_date)

    def __str__(self):
        return 'promo ' + str(self.promo_date)


'''
    create_time = models.DateTimeField(auto_now=True)
    create_user = models.ForeignKey(User, models.SET_NULL, null=True, related_name='promo_creator')
    update_time = models.DateTimeField(blank=True, null=True, default='',)
    update_user = models.ForeignKey(User, models.SET_NULL, null=True, related_name='promo_editor')
    delete_time = models.DateTimeField(blank=True, null=True, default='')
    delete_user = models.ForeignKey(User, models.SET_NULL, null=True, related_name='promo_destroyer')
'''


auditlog.register(GameType)
auditlog.register(GameFunction)
auditlog.register(Role)
auditlog.register(GameResult)
auditlog.register(MemberResult)
auditlog.register(Schedule)
auditlog.register(Location)
auditlog.register(Member)
auditlog.register(Promo)
auditlog.register(RegisteredToGame)
auditlog.register(GameInSchedule)
auditlog.register(MemberInGame)