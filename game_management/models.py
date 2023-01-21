from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage


fs_members = FileSystemStorage(location='files/members')
fs_promo = FileSystemStorage(location='files/promo')
fs_locations = FileSystemStorage(location='files/locations')


class Roles (models.Model):
    role = models.CharField(max_length=40)
    role_description = models.CharField(max_length=255)

    def __repr__(self):
        return self.role + ' ' + self.role_description

    def __str__(self):
        return self.role


class Members (models.Model):
    tg_id = models.IntegerField(default=0)
    tg_name = models.CharField(max_length=255)
    date_birth = models.DateField(default='', blank=True, null=True)
    nickname = models.CharField(max_length=255, default='', null=True, blank=True)
    photo = models.BooleanField(default=False)
    photo_file = models.FileField(storage=fs_members, null=True, blank=True)
    role = models.ForeignKey(Roles, models.SET_NULL)

    def __repr__(self):
        return self.tg_name + ' '+ self.nickname

    def __str__(self):
        return self.nickname


class Location(models.Model):
    location_name = models.CharField(max_length=100)
    location_address = models.CharField(max_length=255)
    Location_directions = models.CharField(max_length=255)

    def __repr__(self):
        return self.location_name

    def __str__(self):
        return self.location_name


class Schedule (models.Model):
    date = models.DateField(auto_now=False)
    time = models.TimeField(auto_now=False)