from django.contrib.auth.models import AbstractUser
from django.db import models

from .validators import validate_username


class User(AbstractUser):

    email = models.EmailField(
        max_length=254,
        unique=True,
        blank=False,
        null=False
    )
    username = models.CharField(
        validators=(validate_username,),
        max_length=150,
        unique=True,
        blank=False,  # обязательое поле
        null=False
    )
    first_name = models.CharField(
        'имя',
        max_length=150,
        blank=False,
        null=False
    )
    last_name = models.CharField(
        'фамилия',
        max_length=150,
        blank=False,
        null=False
    )
    password = models.CharField(
        max_length=150,
        blank=False,
        null=False
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
