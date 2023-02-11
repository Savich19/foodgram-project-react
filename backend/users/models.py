from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.tokens import default_token_generator
from django.db import models
# from django.db.models.signals import post_save
# from django.dispatch import receiver

from .validators import validate_username


class User(AbstractUser):
    # ADMIN = 'admin'
    # GUEST = 'guest'  # не факт, что надо
    # USER = 'user'

    # ROLE_CHOICES = [
    #     (ADMIN, "Администратор"),
    #     (GUEST, "Неавторизованный пользователь"),
    #     (USER, 'Авторизованный пользователь'),
    # ]

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
    # role = models.CharField(
    #     'роль',
    #     max_length=20,
    #     choices=ROLE_CHOICES,
    #     default=USER,
    #     blank=True
    # )
    # confirmation_code = models.CharField(
    #     'код подтверждения',
    #     max_length=255,
    #     null=True,
    #     blank=False,
    #     default='XXXX'
    # )

    class Meta:
        ordering = ['id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
        # return self.username

    # @property
    # def is_user(self):
    #     return self.role == self.USER

    # @property
    # def is_admin(self):
    #     return self.role == self.ADMIN


# @receiver(post_save, sender=User)
# def post_save(sender, instance, created, **kwargs):
#     if created:
#         confirmation_code = default_token_generator.make_token(
#             instance
#         )
#         instance.confirmation_code = confirmation_code
#         instance.save()
