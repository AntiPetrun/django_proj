# Generated by Django 4.1 on 2022-08-06 16:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.datetime_safe
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_name', models.CharField(max_length=50, verbose_name='Название курса')),
                ('teacher', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='Teacher.teacher')),
                ('start_day', models.DateField(default=django.utils.datetime_safe.date.today)),
                ('day_of_week', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], default=None, max_length=50, verbose_name='День недели')),
                ('time', models.TimeField(default=django.utils.timezone.now, verbose_name='Время')),
                ('classroom', models.CharField(max_length=50, verbose_name='Аудитория')),
                ('number_of_lessons', models.PositiveSmallIntegerField(default=0, verbose_name='Кол-во уроков')),
                ('course_type', models.CharField(choices=[('Evening schedule', 'Evening schedule'), ('Morning schedule', 'Morning schedule')], default=None, max_length=50, verbose_name='Вид курса')),
                ('second_teacher', models.BooleanField(verbose_name='Второй преподаватель')),
                ('url', models.SlugField(default=None, max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
    ]