# Generated by Django 3.2.4 on 2021-06-25 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hptl', '0005_alter_booking_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='doctor',
        ),
    ]
