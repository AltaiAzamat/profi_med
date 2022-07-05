# Generated by Django 3.2.9 on 2022-06-12 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Нaзвание')),
                ('anons', models.CharField(max_length=250, verbose_name='Анонс')),
                ('full_text', models.TextField(verbose_name='Cтатья')),
                ('date', models.DateTimeField(verbose_name='ДАта публикации')),
            ],
            options={
                'verbose_name': 'новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
