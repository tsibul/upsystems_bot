# Generated by Django 4.1.5 on 2023-01-23 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game_management', '0005_alter_location_direction_photo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='Location_directions',
            new_name='location_directions',
        ),
    ]
