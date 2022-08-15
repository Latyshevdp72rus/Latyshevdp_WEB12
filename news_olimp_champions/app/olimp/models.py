from django.contrib import admin
from django.db import models


class Stand(models.Model):
    stand_id = ''
    sportsman_id = models.ForeignKey(
        'Sportsman',
        verbose_name="sportsman_id",
        null=False,
        blank=False
    )
    view_olimp_id = models.ForeignKey(
        'ViewOlimp',
        verbose_name="view_olimp_id",
        null=False,
        blank=False
    )
    view_sports_id = models.ForeignKey(
        'ViewSports',
        verbose_name="view_sports_id",
        null=False,
        blank=False
    )
    trener_id = models.ForeignKey(
        'Trener',
        verbose_name="trener_id",
        null=False,
        blank=False
    )
    medal_id = models.ForeignKey(
        'Medal',
        verbose_name="medal_id",
        null=False,
        blank=False
    )
    date_event = models.DateTimeField(
        verbose_name="Дата проведения олимпиады",
        null=True,
        blank=True
    )


class Sportsman(models.Model):
    pass


class ViewOlimp(models.Model):
    pass


class ViewSports(models.Model):
    pass


class Trener(models.Model):
    trener_name=''



class Club(models.Model):
    club_name = models.CharField(
        max_length=30,
        verbose_name="Название клуба")

    club_img =models.ImageField(
        upload_to='media/%y/%m/%d/',
        verbose_name="Загрузить",
        null=True,
        blank=True
    )


class Medal(models.Model):
    medal_name = models.CharField(
        max_length=15,
        verbose_name="Вид медали"
    )
