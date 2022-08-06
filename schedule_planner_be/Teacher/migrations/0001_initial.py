from django.db import migrations, models


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
                ('age', models.PositiveSmallIntegerField(default=0, verbose_name='Возраст')),
                ('experience', models.DateField(verbose_name='Опыт работы')),
                ('group_count', models.PositiveSmallIntegerField(default=0, verbose_name='Количество групп')),
                ('prog_language', models.CharField(max_length=100, verbose_name='Язык программирования')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='Teachers/', verbose_name='Фото')),
            ],
        ),
    ]
