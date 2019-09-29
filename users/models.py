from django.db import models
from django.core.validators import FileExtensionValidator
import datetime

# Create your models here.

class User(models.Model):
    firstname = models.CharField(verbose_name='Имя', max_length=255)
    lastname = models.CharField(verbose_name='Фамилия', max_length=255)
    GENDERS = [
        (1, 'Мужской'),
        (2, 'Женский')
    ]
    gender = models.IntegerField(verbose_name='Пол', choices=GENDERS)
    birth_date = models.DateField(verbose_name='Дата рождения', default=datetime.date.today)
    avatar = models.FileField(verbose_name='Аватар', null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'gif', 'jpeg'])])
    email = models.EmailField(verbose_name='Почта', unique=True, db_index=True, max_length=255)
    password = models.CharField(verbose_name='Пароль', max_length=255)