# Generated by Django 4.1 on 2022-08-21 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olimp', '0019_alter_stand_date_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stand',
            name='date_event',
            field=models.DateField(null=True, verbose_name='Дата олимпиады'),
        ),
    ]
