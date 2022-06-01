# Generated by Django 4.0.4 on 2022-06-01 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('other', '0005_alter_mail1_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mail2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organ', models.CharField(max_length=100, verbose_name='Наименование организации')),
                ('inn', models.CharField(max_length=100, verbose_name='ИНН')),
                ('position', models.CharField(max_length=100, verbose_name='Должность')),
                ('first_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Отчество')),
                ('email', models.CharField(max_length=100, verbose_name='Почта')),
                ('phone', models.CharField(max_length=100, verbose_name='Телефон')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('text', models.TextField(verbose_name='Текст')),
                ('file', models.FileField(blank=True, null=True, upload_to='email_files', verbose_name='Файл')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Обращение Юр лицо',
                'verbose_name_plural': 'Обращения Юр лица',
                'ordering': ['-id'],
            },
        ),
        migrations.AlterModelOptions(
            name='categorycontact',
            options={'ordering': ['-id'], 'verbose_name': 'Название службы', 'verbose_name_plural': 'Название службы'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['-id'], 'verbose_name': 'Контакты', 'verbose_name_plural': 'Контакты'},
        ),
        migrations.AlterModelOptions(
            name='mail1',
            options={'ordering': ['-id'], 'verbose_name': 'Обращение Физ лицо', 'verbose_name_plural': 'Обращения Физ лица'},
        ),
        migrations.AlterModelOptions(
            name='partner',
            options={'ordering': ['-id'], 'verbose_name': 'Партнеры', 'verbose_name_plural': 'Партнеры'},
        ),
    ]
