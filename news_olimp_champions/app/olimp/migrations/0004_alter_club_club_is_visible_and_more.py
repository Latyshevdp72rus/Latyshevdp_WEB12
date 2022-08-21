# Generated by Django 4.1 on 2022-08-21 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olimp', '0003_alter_trener_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='club_is_visible',
            field=models.BooleanField(default=False, verbose_name='Скрыть запись'),
        ),
        migrations.AlterField(
            model_name='medal',
            name='medal_is_visible',
            field=models.BooleanField(default=False, verbose_name='Скрыть запись'),
        ),
        migrations.AlterField(
            model_name='sportsman',
            name='sportsman_is_visible',
            field=models.BooleanField(default=False, verbose_name='Скрыть запись'),
        ),
        migrations.AlterField(
            model_name='stand',
            name='stand_is_visible',
            field=models.BooleanField(default=False, verbose_name='Скрыть запись'),
        ),
        migrations.AlterField(
            model_name='trener',
            name='trener_is_visible',
            field=models.BooleanField(default=False, verbose_name='Скрыть запись'),
        ),
        migrations.AlterField(
            model_name='viewolimp',
            name='view_olimp_is_visble',
            field=models.BooleanField(default=False, verbose_name='Скрыть запись'),
        ),
        migrations.AlterField(
            model_name='viewsports',
            name='view_sports_is_visible',
            field=models.BooleanField(default=False, verbose_name='Скрыть запись'),
        ),
    ]
