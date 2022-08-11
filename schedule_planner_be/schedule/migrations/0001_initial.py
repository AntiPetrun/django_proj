

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50, verbose_name='Город')),
                ('street', models.CharField(max_length=50, verbose_name='Улица')),
                ('building', models.IntegerField(default=None, verbose_name='Номер дома')),
            ],
            options={
                'verbose_name': 'Локация',
                'verbose_name_plural': 'Локации',
            },
        ),
        migrations.CreateModel(
            name='SubwayStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

                ('station', models.CharField(default=None, max_length=50)),

            ],
            options={
                'verbose_name': 'Станция метро',
                'verbose_name_plural': 'Станции метро',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

                ('title', models.TextField(default=None)),
                ('url', models.URLField(default=None, max_length=160, unique=True)),
                ('courses', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='course.course', verbose_name='Курсы')),
                ('locations', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='schedule.location', verbose_name='Локации')),
                ('reviews', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='course.comment', verbose_name='Комментарии')),

            ],
            options={
                'verbose_name': 'Расписание',
                'verbose_name_plural': 'Расписания',
            },
        ),
        migrations.AddField(
            model_name='location',
            name='subway',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='schedule.subwaystation', verbose_name='Станции метро'),
        ),
    ]
