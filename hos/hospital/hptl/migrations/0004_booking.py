# Generated by Django 3.2.4 on 2021-06-23 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hptl', '0003_delete_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('num', models.TextField()),
                ('address', models.TextField()),
                ('created', models.DateTimeField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hptl.doctor')),
            ],
        ),
    ]
