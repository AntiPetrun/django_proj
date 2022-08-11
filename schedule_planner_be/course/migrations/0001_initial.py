

from django.db import migrations, models
import django.utils.datetime_safe
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='Комментарий')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50, verbose_name='Название курса')),
                ('start_day', models.DateField(default=django.utils.datetime_safe.date.today)),
                ('day_of_week', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], default=None, max_length=50, verbose_name='День недели')),
                ('time', models.TimeField(default=django.utils.timezone.now, verbose_name='Время')),
                ('classroom', models.CharField(max_length=50, verbose_name='Аудитория')),
                ('number_of_lessons', models.PositiveSmallIntegerField(default=0, verbose_name='Кол-во уроков')),
                ('course_type', models.CharField(choices=[('Evening schedule', 'Evening schedule'), ('Morning schedule', 'Morning schedule')], default=None, max_length=50, verbose_name='Вид курса')),
                ('second_teacher', models.BooleanField(verbose_name='Второй преподаватель')),
                ('url', models.URLField(default=None, max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
    ]
