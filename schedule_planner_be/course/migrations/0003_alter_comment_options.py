# Generated by Django 4.1 on 2022-08-06 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('created',), 'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
    ]
