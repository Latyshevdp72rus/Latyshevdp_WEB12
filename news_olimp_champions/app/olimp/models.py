from PIL import Image
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.base_user import BaseUserManager


class Stand(models.Model):
    stand_name = models.CharField(
        max_length=40,
        verbose_name="Заголовок записи",
        null=False,
        blank=False,
    )
    stand_description = models.TextField(
        verbose_name="Описание",
        max_length=1000,
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
        verbose_name="Страна спортсмена",
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
        default="media/default.png",
        verbose_name="Загрузить фото",
        null=False,
        blank=True,
    )
    sportsman_is_visible = models.BooleanField(
        default=False,
        verbose_name="Скрытая запись",
        null=True,
        blank=True,
    )

    def save(self):
        super().save()
        sportsman_images = Image.open(self.sportsman_img.path)
        if sportsman_images.height > 250 or sportsman_images.width > 200:
            output_size = (200, 250)
            sportsman_images.thumbnail(output_size)
            sportsman_images.save(self.sportsman_img.path)

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
        default="media/default.png",
        verbose_name="Загрузить фото",
        null=False,
        blank=True,
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

    def save(self):
        super().save()
        trener_images = Image.open(self.trener_img.path)
        if trener_images.height > 250 or trener_images.width > 200:
            output_size = (200, 250)
            trener_images.thumbnail(output_size)
            trener_images.save(self.trener_img.path)

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
        default="media/default.png",
        null=False,
        blank=True,
    )
    club_is_visible = models.BooleanField(
        default=False,
        verbose_name="Скрытая запись",
        null=True,
        blank=True,
    )

    def save(self):
        super().save()
        club_images = Image.open(self.club_img.path)
        if club_images.height > 250 or club_images.width > 200:
            output_size = (200, 250)
            club_images.thumbnail(output_size)
            club_images.save(self.club_img.path)

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

    def __str__(self):
        return self.medal_name

    class Meta:
        verbose_name = "МЕДАЛЬ"
        verbose_name_plural = "МЕДАЛИ"


class FeedBack(models.Model):
    fb_name = models.CharField(
        max_length=50,
        verbose_name="Как к Вам обращаться:",
        null=False,
        blank=False,
    )
    fb_email = models.EmailField(
        verbose_name="Email для связи:",
        null=False,
        blank=False,
    )
    fb_message = models.TextField(
        verbose_name="Ваше сообщение:",
        null=False,
        blank=False,
    )
    date_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата добавления",
        null=True,
        blank=True,
    )
    fb_img = models.ImageField(
        upload_to="media/feedback/%y/%m/%d/",
        verbose_name="Загрузить фото",
        null=True,
        blank=True,
    )

    def save(self):
        super().save()
        fb_images = Image.open(self.fb_img.path)
        if fb_images.height > 250 or fb_images.width > 200:
            output_size = (200, 250)
            fb_images.thumbnail(output_size)
            fb_images.save(self.fb_img.path)

    def __str__(self):
        return self.fb_name

    class Meta:
        verbose_name = "ОБРАТНАЯ СВЯЗЬ"
        verbose_name_plural = "ОБРАТНАЯ СВЯЗЬ"


class CommentsSportsman(models.Model):
    """ Класс коментарий на странице спортсмена"""
    # user

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    news = models.ForeignKey(
        Sportsman,
        verbose_name="Новость",
        on_delete=models.CASCADE
    )
    text = models.TextField(verbose_name="Комментарии")
    date_created = models.DateTimeField(
        verbose_name="Дата добавления",
        blank=True,
        null=True,
        auto_now_add=True,
    )
    moderation_is_visible = models.BooleanField(
        default=False,
        verbose_name="Скрытая запись",
        null=True,
        blank=True,
    )

    def __str__(self):
        return "{} - {} ({})".format(self.user,self.news,self.date_created)

    class Meta:
        db_table = "CommentsSportsman"
        verbose_name = "Коментарий"
        verbose_name_plural = "Коментарии"
