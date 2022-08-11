

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('surname', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('age', models.PositiveSmallIntegerField(default=0, verbose_name='Возраст')),
                ('start_date', models.DateField()),
                ('group_count', models.PositiveSmallIntegerField(default=0, verbose_name='Количество групп')),
                ('prog_language', models.CharField(max_length=100, verbose_name='Язык программирования')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='Media/Teachers/', verbose_name='Фото')),
                ('url', models.SlugField(default=None, max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Преподаватель',
                'verbose_name_plural': 'Преподаватели',
                'db_table': 'teacher',
            },
        ),
        migrations.CreateModel(
            name='TeacherProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.CharField(blank=True, max_length=50, null=True)),
                ('twitter', models.CharField(blank=True, max_length=50, null=True)),
                ('instagram', models.CharField(blank=True, max_length=50, null=True)),
                ('teacher', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Teacher.teacher')),
            ],
            options={
                'verbose_name': 'Профиль преподавателя',
                'verbose_name_plural': 'Профили преподавателей',
                'db_table': 'teacher_profile',
            },
        ),
    ]
