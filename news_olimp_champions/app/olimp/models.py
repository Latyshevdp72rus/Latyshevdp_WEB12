from django.contrib import admin
from django.db import models


class Stand(models.Model):
    stand_name = models.CharField(
        max_length=20,
        verbose_name="Заголовок записи",
        null=False,
        blank=False,
    )
    stand_description = models.TextField(
        verbose_name="Описание записи",
        max_length=100,
        null=False,
        blank=False,
    )
    sportsman_id = models.ForeignKey(
        "Sportsman",
        on_delete=models.CASCADE,
        related_name="Sportsman_Stand",
        verbose_name="Спортсмен",
        null=False,
        blank=False,
    )
    view_olimp_id = models.ForeignKey(
        "ViewOlimp",
        on_delete=models.CASCADE,
        related_name="ViewOlimp_Stand",
        verbose_name="Вид олимпийских игр",
        null=False,
        blank=False,
    )
    medal_id = models.ForeignKey(
        "Medal",
        on_delete=models.CASCADE,
        related_name="Medal_Stand",
        verbose_name="Медаль",
        null=False,
        blank=False,
    )
    date_event = models.DateField(
        verbose_name="Дата олимпиады",
        null=True,
        blank=False,
    )
    stand_is_visible = models.BooleanField(
        default=False,
        verbose_name="Скрытая запись",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.stand_name

    class Meta:
        verbose_name = "СТЕНД"
        verbose_name_plural = "СТЕНД"


class Sportsman(models.Model):
    sportsman_name = models.CharField(
        max_length=50,
        verbose_name="ФИО спортсмена",
        null=False,
        blank=False,
    )
    sportsman_country = models.CharField(
        max_length=30,
        verbose_name="Страна",
        null=False,
        blank=False,
    )
    sportsman_birthday = models.DateField(
        max_length=8,
        verbose_name="Дата рождения",
        null=False,
        blank=False,
    )
    sportsman_biogrpahy = models.TextField(
        verbose_name="Биография",
        null=True,
        blank=True,
    )
    view_sports_id = models.ForeignKey(
        "ViewSports",
        on_delete=models.CASCADE,
        related_name="ViewSports_Sportsman",
        verbose_name="Вид спорта",
        null=False,
        blank=False,
    )
    trener_id = models.ForeignKey(
        "Trener",
        on_delete=models.CASCADE,
        related_name="Trener_Sportsman",
        verbose_name="Тренер",
        null=False,
        blank=False,
    )
    sportsman_img = models.ImageField(
        upload_to="media/sportsman/%y/%m/%d/",
        verbose_name="Загрузить фото",
        null=False,
        blank=False,
    )
    sportsman_is_visible = models.BooleanField(
        default=False,
        verbose_name="Скрытая запись",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.sportsman_name

    class Meta:
        verbose_name = "СПОРТСМЕНА"
        verbose_name_plural = "СПОРТСМЕНЫ"


class ViewOlimp(models.Model):
    view_olimp_name = models.CharField(
        max_length=50,
        verbose_name="Наименование олимпийских игр",
         null=False,
         blank=False,
    )
    view_olimp_is_visible = models.BooleanField(
        default=False,
        verbose_name="Скрытая запись",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.view_olimp_name

    class Meta:
        verbose_name = "ВИД ОЛИМПИЙСКИХ ИГР"
        verbose_name_plural = "ВИДЫ ОЛИМПИЙСКИХ ИГР"


class ViewSports(models.Model):
   view_sport_name = models.CharField(
       max_length=50,
       verbose_name="Наименование вида спорта",
       null=False,
       blank=False,
    )
   view_sports_is_visible = models.BooleanField(
       default=False,
       verbose_name="Скрытая запись",
       null=True,
       blank=True,
   )
   def __str__(self):
        return self.view_sport_name

   class Meta:
        verbose_name = "ВИД СПОРТА"
        verbose_name_plural = "ВИД СПОРТА"


class Trener(models.Model):
    trener_name = models.CharField(
        max_length=50,
        verbose_name="ФИО тренера",
        null=False,
        blank=False,
    )
    trener_img = models.ImageField(
        upload_to="media/trener/%y/%m/%d/",
        verbose_name="Загрузить фото",
        null=False,
        blank=False,
    )
    club_id = models.ForeignKey(
        "Club",
        on_delete=models.CASCADE,
        related_name="Club_Trener",
        verbose_name="Клуб",
        null=False,
        blank=False,
    )
    trener_is_visible = models.BooleanField(
        default=False,
        verbose_name="Скрытая запись",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.trener_name

    class Meta:
        verbose_name = "ТРЕНЕРА"
        verbose_name_plural = "ТРЕНЕРЫ"


class Club(models.Model):
    club_name = models.CharField(
        max_length=30,
        verbose_name="Название клуба",
        null=False,
        blank=False,
    )
    club_img = models.ImageField(
        upload_to="media/club/%y/%m/%d/",
        verbose_name="Загрузить логотип",
        null=False,
        blank=False,
    )
    club_is_visible = models.BooleanField(
        default=False,
        verbose_name="Скрытая запись",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.club_name

    class Meta:
        verbose_name = "КЛУБ"
        verbose_name_plural = "КЛУБЫ"


class Medal(models.Model):
    medal_name = models.CharField(
        max_length=20,
        verbose_name="Вид медали",
        null=False,
        blank=False,
    )
    medal_is_visible = models.BooleanField(
        default=False,
        verbose_name="Скрытая запись",
        null=True,
        blank=True,
    )
    def __str__(self):
        return self.medal_name

    class Meta:
        verbose_name = "МЕДАЛЬ"
        verbose_name_plural = "МЕДАЛИ"
