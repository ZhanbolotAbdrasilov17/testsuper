# Generated by Django 4.0.4 on 2022-06-01 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_about_tasktext_taskimage_powertext_power_aboutvideo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GosOrgan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('link', models.CharField(max_length=200, verbose_name='Ссылка на сайт')),
                ('image', models.ImageField(upload_to='gos-organ', verbose_name='Логотип')),
            ],
            options={
                'verbose_name': 'Гос органы',
                'verbose_name_plural': 'Гос органы',
                'ordering': ['-id'],
            },
        ),
        migrations.AlterModelOptions(
            name='about',
            options={'ordering': ['-id'], 'verbose_name': 'О нас', 'verbose_name_plural': 'О нас'},
        ),
        migrations.AlterModelOptions(
            name='home',
            options={'ordering': ['-id'], 'verbose_name': 'Главная', 'verbose_name_plural': 'Главная'},
        ),
    ]
