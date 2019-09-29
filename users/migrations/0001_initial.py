# Generated by Django 2.2.5 on 2019-09-29 12:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255, verbose_name='Имя')),
                ('lastname', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('gender', models.IntegerField(choices=[(1, 'Мужской'), (2, 'Женский')], verbose_name='Пол')),
                ('birth_date', models.DateField(default=datetime.date.today)),
                ('email', models.EmailField(db_index=True, max_length=255, unique=True, verbose_name='Email')),
                ('password', models.CharField(max_length=255, verbose_name='')),
            ],
        ),
    ]