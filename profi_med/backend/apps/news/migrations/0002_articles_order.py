# Generated by Django 3.2.9 on 2022-06-25 10:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Нaзвание')),
                ('anons', models.CharField(max_length=250, verbose_name='Анонс')),
                ('full_text', models.TextField(verbose_name='Cтатья')),
                ('date', models.DateTimeField(verbose_name='Дaта публикации')),
            ],
            options={
                'verbose_name': 'новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('postal_code', models.CharField(max_length=10, verbose_name='Почтовый индекс')),
                ('mobile', models.CharField(max_length=10, verbose_name='Номер телефона')),
                ('notice', models.CharField(max_length=255, verbose_name='Комментарий')),
                ('status', models.CharField(choices=[('new', 'Новый'), ('confirmed', 'Подтвержден'), ('send', 'Отправлен'), ('delivered', 'Доставлен'), ('rejected', 'Отменен')], default='new', max_length=9, verbose_name='Статус')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]