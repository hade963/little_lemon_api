# Generated by Django 4.2.7 on 2024-02-29 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resturant', '0003_alter_booking_no_of_guests'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='Pirce',
            new_name='Price',
        ),
    ]
