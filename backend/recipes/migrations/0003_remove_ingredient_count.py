# Generated by Django 4.1.5 on 2023-02-11 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20230211_0652'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='count',
        ),
    ]
