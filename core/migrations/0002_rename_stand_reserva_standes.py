# Generated by Django 4.2.4 on 2023-09-01 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reserva',
            old_name='stand',
            new_name='standes',
        ),
    ]
