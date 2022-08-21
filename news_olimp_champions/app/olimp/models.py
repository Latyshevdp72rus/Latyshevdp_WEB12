from django.contrib import admin
from django.db import models


class Stand(models.Model):
    stand_name = models.CharField(
        max_length=50,
        verbose_name="Заголовок стэнда: "
    )
    stand_description = models.TextField(
        verbose_name="Описание стэнда: ",
        null=True,
        blank=True
    )
    sportsman_id = models.ForeignKey(
        "Sportsman",
        on_delete=models.CASCADE,
        related_name="Sportsman_Stand",
        verbose_name="sportsman_id: ",
        null=True,
        blank=True
    )
    view_olimp_id = models.ForeignKey(
        "ViewOlimp",
        on_delete=models.CASCADE,
        related_name="ViewOlimp_Stand",
        verbose_name="view_olimp_id: ",
        null=True,
        blank=True
    )
    medal_id = models.ForeignKey(
        "Medal",
        on_delete=models.CASCADE,
        related_name="Medal_Stand",
        verbose_name="medal_id: ",
        null=True,
        blank=True
    )
    date_event = models.DateTimeField(
        verbose_name="Дата проведения олимпиады",
        null=True,
        blank=True
    )
    stand_is_visible = models.BooleanField(
        default=False,
        verbose_name="Скрыть запись: "
    )

    def __str__(self):
        return self.stand_name

    class Meta:
        verbose_name = "СТЕНД"
        verbose_name_plural = "СТЕНДЫ"


class Sportsman(models.Model):
    sportsman_name = models.CharField(
        max_length=50,
        verbose_name="ФИО спортсмена: "
    )
    sportsman_country = models.CharField(
        max_length=30,
        verbose_name="Страна: "
    )
    sportsman_birthday = models.DateField(
        max_length=8,
        verbose_name="Дата рождения"
    )
    sportsman_biogrpahy = models.TextField(
        verbose_name="Описание книги: ",
        null=True,
        blank=True
    )
    view_sports_id = models.ForeignKey(
        "ViewSports",
        on_delete=models.CASCADE,
        related_name="ViewSports_Sportsman",
        verbose_name="view_sports_id: ",
        null=True,
        blank=True
    )
    trener_id = models.ForeignKey(
        "Trener",
        on_delete=models.CASCADE,
        related_name="Trener_Sportsman",
        verbose_name="view_sports_id: ",
        null=True,
        blank=True
    )
    sportsman_img = models.ImageField(
        upload_to="media/trener/%y/%m/%d/",
        verbose_name="Загрузить фото: ",
        null=True,
        blank=True
    )
    sportsman_is_visible = models.BooleanField(
        default=False,
        verbose_name="Скрыть запись: "
    )

    def __str__(self):
        return self.sportsman_name

    class Meta:
        verbose_name = "СПОРТСМЕН"
        verbose_name_plural = "СПОРТСМЕНЫ"


class ViewOlimp(models.Model):
    view_olimp_name = models.CharField(
        max_length=50,
        verbose_name="Наименование олимпийских игр: "
    )
    view_olimp_is_visble = models.BooleanField(
        default=False,
        verbose_name="Скрыть запись: "
    )

    def __str__(self):
        return self.view_olimp_name

    class Meta:
        verbose_name = "ВИД ОЛИМПИЙСКИХ ИГР"
        verbose_name_plural = "ВИД ОЛИМПИЙСКИХ ИГР"


class ViewSports(models.Model):
   view_sport_name = models.CharField(
        max_length=50,
        verbose_name="Наименование вида спорта: "
    )
   view_sports_is_visible = models.BooleanField(
       default=False,
       verbose_name="Скрыть запись: "
   )
   def __str__(self):
        return self.view_sport_name

   class Meta:
        verbose_name = "ВИД СПОРТА"
        verbose_name_plural = "ВИД СПОРТА"


class Trener(models.Model):
    trener_name = models.CharField(
        max_length=50,
        verbose_name="ФИО тренера: "
    )
    trener_img = models.ImageField(
        upload_to="media/trener/%y/%m/%d/",
        verbose_name="Загрузить фото: ",
        null=True,
        blank=True
    )
    club_id = models.ForeignKey(
        "Club",
        on_delete=models.CASCADE,
        related_name="Club_Trener",
        verbose_name="club_id: ",
        null=True,
        blank=True
    )
    trener_is_visible = models.BooleanField(
        default=False,
        verbose_name="Скрыть запись: "
    )

    def __str__(self):
        return self.trener_name

    class Meta:
        verbose_name = "ТРЕНЕР"
        verbose_name_plural = "ТРЕНЕРА"


class Club(models.Model):
    club_name = models.CharField(
        max_length=30,
        verbose_name="Название клуба: "
    )
    club_img = models.ImageField(
        upload_to="media/club/%y/%m/%d/",
        verbose_name="Загрузить логотип: ",
        null=True,
        blank=True
    )
    club_is_visible = models.BooleanField(
        default=False,
        verbose_name="Скрыть запись: "
    )

    def __str__(self):
        return self.club_name

    class Meta:
        verbose_name = "КЛУБ"
        verbose_name_plural = "КЛУБЫ"


class Medal(models.Model):
    medal_name = models.CharField(
        max_length=15,
        verbose_name="Вид медали: "
    )
    medal_is_visible = models.BooleanField(
        default=False,
        verbose_name="Скрыть запись: "
    )
    def __str__(self):
        return self.medal_name

    class Meta:
        verbose_name = "МЕДАЛЬ"
        verbose_name_plural = "МЕДАЛИ"
