# Generated by Django 3.2.9 on 2022-07-04 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_articles_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]
