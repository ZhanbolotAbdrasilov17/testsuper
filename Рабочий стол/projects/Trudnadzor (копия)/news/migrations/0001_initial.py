# Generated by Django 4.0.4 on 2022-04-13 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('title', models.CharField(max_length=500, verbose_name='Заголовок')),
                ('announcement', models.CharField(blank=True, max_length=200, null=True, verbose_name='Анонс')),
                ('image', models.ImageField(upload_to='news_images', verbose_name='Фото')),
            ],
        ),
    ]
