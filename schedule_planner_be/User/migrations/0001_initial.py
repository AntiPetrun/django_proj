# Generated by Django 4.1 on 2022-08-08 11:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('SuperAdmin', 'SuperAdmin'), ('Administrator', 'Administrator'), ('Manager', 'Manager'), ('Teacher', 'Teacher')], max_length=15, null=True, verbose_name='Роль')),
                ('fist_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=150, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_email', message='Write correct email address', regex="^([A-Za-z0-9]{1}[-!#$%&'*+./=?^_`{}|~A-Za-z0-9]{,63})@([a-z]{1,}\\.){1,2}[a-z]{2,6}$")])),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
