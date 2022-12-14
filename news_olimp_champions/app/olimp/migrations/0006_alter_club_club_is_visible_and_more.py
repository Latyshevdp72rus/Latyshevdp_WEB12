# Generated by Django 4.1 on 2022-08-21 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('olimp', '0005_alter_club_options_alter_medal_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='club_is_visible',
            field=models.BooleanField(default=False, verbose_name='Скрыть запись: '),
        ),
        migrations.AlterField(
            model_name='medal',
            name='medal_is_visible',
            field=models.BooleanField(default=False, verbose_name='Скрыть запись: '),
        ),
        migrations.AlterField(
            model_name='sportsman',
            name='sportsman_biogrpahy',
            field=models.TextField(blank=True, null=True, verbose_name='Описание книги: '),
        ),
        migrations.AlterField(
            model_name='sportsman',
            name='sportsman_country',
            field=models.CharField(max_length=30, verbose_name='Страна: '),
        ),
        migrations.AlterField(
            model_name='sportsman',
            name='sportsman_is_visible',
            field=models.BooleanField(default=False, verbose_name='Скрыть запись: '),
        ),
        migrations.AlterField(
            model_name='sportsman',
            name='trener_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Trener_Sportsman', to='olimp.trener', verbose_name='view_sports_id: '),
        ),
        migrations.AlterField(
            model_name='sportsman',
            name='view_sports_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ViewSports_Sportsman', to='olimp.viewsports', verbose_name='view_sports_id: '),
        ),
        migrations.AlterField(
            model_name='stand',
            name='medal_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Medal_Stand', to='olimp.medal', verbose_name='medal_id: '),
        ),
        migrations.AlterField(
            model_name='stand',
            name='sportsman_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Sportsman_Stand', to='olimp.sportsman', verbose_name='sportsman_id: '),
        ),
        migrations.AlterField(
            model_name='stand',
            name='stand_description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание стэнда: '),
        ),
        migrations.AlterField(
            model_name='stand',
            name='stand_is_visible',
            field=models.BooleanField(default=False, verbose_name='Скрыть запись: '),
        ),
        migrations.AlterField(
            model_name='stand',
            name='view_olimp_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ViewOlimp_Stand', to='olimp.viewolimp', verbose_name='view_olimp_id: '),
        ),
        migrations.AlterField(
            model_name='trener',
            name='club_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Club_Trener', to='olimp.club', verbose_name='club_id: '),
        ),
        migrations.AlterField(
            model_name='trener',
            name='trener_is_visible',
            field=models.BooleanField(default=False, verbose_name='Скрыть запись: '),
        ),
        migrations.AlterField(
            model_name='viewolimp',
            name='view_olimp_is_visble',
            field=models.BooleanField(default=False, verbose_name='Скрыть запись: '),
        ),
        migrations.AlterField(
            model_name='viewsports',
            name='view_sports_is_visible',
            field=models.BooleanField(default=False, verbose_name='Скрыть запись: '),
        ),
    ]
