# Generated by Django 4.1 on 2022-09-11 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olimp', '0030_remove_medal_medal_is_visible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stand',
            name='stand_description',
            field=models.TextField(max_length=1000, verbose_name='Описание записи'),
        ),
    ]
