from django.contrib import admin
from django.db import models


class Stand(models.Model):
    stand_id = ''
    sportsman_id = models.ForeignKey(
        'Sportsman',
        on_delete=models.CASCADE,
        related_name='',
        verbose_name="sportsman_id",
        null=True,
        blank=True
    )
    view_olimp_id = models.ForeignKey(
        'ViewOlimp',
        on_delete=models.CASCADE,
        related_name='',
        verbose_name="view_olimp_id",
        null=True,
        blank=True
    )
    view_sports_id = models.ForeignKey(
        'ViewSports',
        on_delete=models.CASCADE,
        related_name='',
        verbose_name="view_sports_id",
        null=True,
        blank=True
    )
    trener_id = models.ForeignKey(
        'Trener',
        on_delete=models.CASCADE,
        related_name='',
        verbose_name="trener_id",
        null=True,
        blank=True
    )
    medal_id = models.ForeignKey(
        'Medal',
        on_delete=models.CASCADE,
        related_name='',
        verbose_name="medal_id",
        null=True,
        blank=True
    )
    date_event = models.DateTimeField(
        verbose_name="Дата проведения олимпиады",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Стенд'
        verbose_name_plural = 'Стенд'

class Sportsman(models.Model):
    pass
    class Meta:
        verbose_name = 'Спортсмен'
        verbose_name_plural = 'Спортсмена'

class ViewOlimp(models.Model):
    pass


class ViewSports(models.Model):
    pass


class Trener(models.Model):
    trener_name = ''
    trener_img = models.ImageField(
        upload_to='media/phototrener/%y/%m/%d/',
        verbose_name="Загрузить фото: ",
        null=True,
        blank=True
    )
    club_id = models.ForeignKey(
        'Club',
        on_delete=models.CASCADE,
        related_name='',
        verbose_name="club_id",
        null=True,
        blank=True
    )


class Club(models.Model):
    club_name = models.CharField(
        max_length=30,
        verbose_name="Название клуба"
    )
    club_img = models.ImageField(
        upload_to='media/club/%y/%m/%d/',
        verbose_name="Загрузить логотип: ",
        null=True,
        blank=True
    )


class Medal(models.Model):
    medal_name = models.CharField(
        max_length=15,
        verbose_name="Вид медали"
    )
