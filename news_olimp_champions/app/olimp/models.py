from PIL import Image
from django.contrib.auth.models import User
from django.db import models


class Stand(models.Model):
    """ Класс на странице НОВОСТИ """
    stand_name = models.CharField(
        verbose_name="Заголовок новости",
        max_length=50,
        null=False,
        blank=False,
    )
    stand_description = models.TextField(
        verbose_name="Описание новости",
        max_length=1000,
        null=False,
        blank=False,
    )
    sportsman_id = models.ForeignKey(
        "Sportsman",
        related_name="Sportsman_Stand",
        verbose_name="Спортсмен",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )
    view_olimp_id = models.ForeignKey(
        "ViewOlimp",
        related_name="ViewOlimp_Stand",
        verbose_name="Вид олимпийских игр",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )
    medal_id = models.ForeignKey(
        "Medal",
        related_name="Medal_Stand",
        verbose_name="Медаль",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )
    date_event = models.DateField(
        verbose_name="Дата олимпиады",
        null=False,
        blank=False,
    )
    date_created = models.DateField(
        verbose_name="Дата добавления",
        auto_now_add=True,
        blank=False,
        null=False,
    )
    stand_img = models.ImageField(
        verbose_name="Загрузить фото",
        default="media/default.png",
        upload_to="media/stand/%y/%m/%d/",
        null=True,
        blank=True,
    )
    stand_is_visible = models.BooleanField(
        verbose_name="Скрыть запись",
        default=False,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.stand_name

    class Meta:
        verbose_name = "СТЕНД"
        verbose_name_plural = "СТЕНД"


class CommentsStand(models.Model):
    """ Класс коментарий на странице НОВОСТИ """
    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )
    news = models.ForeignKey(
        Stand,
        verbose_name="Новость спортсмена",
        null = False,
        blank = False,
        on_delete=models.CASCADE,
    )
    text = models.TextField(
        verbose_name="Комментарии",
        max_length = 1000,
        null = False,
        blank = False,
    )
    date_created = models.DateTimeField(
        verbose_name="Дата добавления",
        auto_now_add=True,
        blank=False,
        null=False,
    )
    moderation_is_visible = models.BooleanField(
        verbose_name="Скрыть запись",
        default=False,
        null=True,
        blank=True,
    )

    def __str__(self):
        return "{} - {} ({})".format(self.user, self.news, self.date_created)

    class Meta:
        verbose_name = "КОММЕНТАРИЙ НОВОСТЕЙ"
        verbose_name_plural = "КОММЕНТАРИИ НОВОСТЕЙ"


class Sportsman(models.Model):
    sportsman_name = models.CharField(
        verbose_name="ФИО спортсмена",
        max_length=50,
        null=False,
        blank=False,
    )
    country_id = models.ForeignKey(
        "Country",
        related_name="Country_Sportsman",
        verbose_name="Страна спортсмена",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )
    sportsman_birthday = models.DateField(
        verbose_name="Дата рождения",
        max_length=8,
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
        related_name="ViewSports_Sportsman",
        verbose_name="Вид спорта",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )
    trener_id = models.ForeignKey(
        "Trener",
        related_name="Trener_Sportsman",
        verbose_name="Тренер",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )
    date_created = models.DateField(
        verbose_name="Дата добавления",
        auto_now_add=True,
        blank=False,
        null=False,
    )
    sportsman_img = models.ImageField(
        verbose_name="Загрузить фото",
        default="media/default.png",
        upload_to="media/sportsman/%y/%m/%d/",
        null=True,
        blank=True,
    )
    sportsman_is_visible = models.BooleanField(
        verbose_name="Скрыть запись",
        default=False,
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


class CommentsSportsman(models.Model):
    """ Класс коментарий на странице спортсмена"""
    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )
    news = models.ForeignKey(
        Sportsman,
        verbose_name="Новость спортсмена",
        null = False,
        blank = False,
        on_delete=models.CASCADE,
    )
    text = models.TextField(
        verbose_name="Комментарии",
        max_length = 1000,
        null = False,
        blank = False,
    )
    date_created = models.DateTimeField(
        verbose_name="Дата добавления",
        auto_now_add=True,
        blank=False,
        null=False,

    )
    moderation_is_visible = models.BooleanField(
        verbose_name="Скрыть запись",
        default=False,
        null=True,
        blank=True,
    )

    def __str__(self):
        return "{} - {} ({})".format(self.user, self.news, self.date_created)

    class Meta:
        verbose_name = "КОММЕНТАРИЙ СПОРТСМЕНА"
        verbose_name_plural = "КОММЕНТАРИИ СПОРТСМЕНА"


class Trener(models.Model):
    """ Класс медали"""
    trener_name = models.CharField(
        verbose_name="ФИО тренера",
        max_length=50,
        null=False,
        blank=False,
    )
    club_id = models.ForeignKey(
        "Club",
        related_name="Club_Trener",
        verbose_name="Клуб",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )
    date_created = models.DateField(
        verbose_name="Дата добавления",
        auto_now_add=True,
        blank=False,
        null=False,
    )
    trener_img = models.ImageField(
        default="media/default.png",
        upload_to="media/trener/%y/%m/%d/",
        verbose_name="Загрузить фото",
        null=True,
        blank=True,
    )

    trener_is_visible = models.BooleanField(
        verbose_name="Скрыть запись",
        default=False,
        null=True,
        blank=True,
    )

    def save(self):
        super().save()
        trener_images = Image.open(self.trener_img.path)
        if trener_images.height > 250 or trener_images.width > 187:
            output_size = (187, 250)
            trener_images.thumbnail(output_size)
            trener_images.save(self.trener_img.path)

    def __str__(self):
        return self.trener_name

    class Meta:
        verbose_name = "ТРЕНЕРА"
        verbose_name_plural = "ТРЕНЕРЫ"


class CommentsTrener(models.Model):
    """ Класс коментарий на странице Тренера"""
    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )
    news = models.ForeignKey(
        Trener,
        verbose_name="Новость тренера",
        null = False,
        blank = False,
        on_delete=models.CASCADE,
    )
    text = models.TextField(
        verbose_name="Комментарии",
        max_length = 1000,
        null = False,
        blank = False,
    )
    date_created = models.DateTimeField(
        verbose_name="Дата добавления",
        auto_now_add=True,
        blank=False,
        null=False,

    )
    moderation_is_visible = models.BooleanField(
        verbose_name="Скрыть запись",
        default=False,
        null=True,
        blank=True,
    )

    def __str__(self):
        return "{} - {} ({})".format(self.user, self.news, self.date_created)

    class Meta:
        verbose_name = "КОММЕНТАРИЙ ТРЕНЕРА"
        verbose_name_plural = "КОММЕНТАРИИ ТРЕНЕРА"


class ViewOlimp(models.Model):
    view_olimp_name = models.CharField(
        verbose_name="Наименование олимпийских игр",
        max_length=50,
        null=False,
        blank=False,
    )
    view_olimp_is_visible = models.BooleanField(
        verbose_name="Скрыть запись",
        default=False,
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
        verbose_name="Наименование вида спорта",
        max_length=50,
        null=False,
        blank=False,
    )
    view_sports_is_visible = models.BooleanField(
        verbose_name="Скрыть запись",
        default=False,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.view_sport_name

    class Meta:
        verbose_name = "ВИД СПОРТА"
        verbose_name_plural = "ВИД СПОРТА"


class Club(models.Model):
    """ Класс клуб"""
    club_name = models.CharField(
        verbose_name="Название клуба",
        max_length=30,
        null=False,
        blank=False,
    )
    club_img = models.ImageField(
        verbose_name="Загрузить логотип",
        default="media/default.png",
        upload_to="media/club/%y/%m/%d/",
        null=True,
        blank=True,
    )
    club_is_visible = models.BooleanField(
        verbose_name="Скрыть запись",
        default=False,
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
    """ Класс медали"""
    medal_name = models.CharField(
        verbose_name="Вид медали",
        max_length=20,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.medal_name

    class Meta:
        verbose_name = "МЕДАЛЬ"
        verbose_name_plural = "МЕДАЛИ"


class FeedBack(models.Model):
    """ Класс обратной связи"""
    fb_name = models.CharField(
        verbose_name="Как к Вам обращаться:",
        max_length=50,
        null=False,
        blank=False,
    )
    fb_email = models.EmailField(
        verbose_name="Email для связи:",
        max_length=30,
        null=False,
        blank=False,
    )
    fb_message = models.TextField(
        verbose_name="Ваше сообщение:",
        max_length=1000,
        null=False,
        blank=False,
    )
    date_create = models.DateTimeField(
        verbose_name="Дата добавления",
        auto_now_add=True,
        null=False,
        blank=False,
    )
    fb_img = models.ImageField(
        verbose_name="Загрузить фото",
        default="media/default.png",
        upload_to="media/feedback/%y/%m/%d/",
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


class Country(models.Model):
    """ Класс Страны"""
    country_name = models.CharField(
        verbose_name="Страна",
        max_length=50,
        null=True,
        blank=True,
    )
    country_img = models.ImageField(
        verbose_name="Загрузить флаг",
        # default="media/default.png",
        upload_to="media/flags/%y/%m/%d/",
        null=True,
        blank=True,
    )
    country_is_visible = models.BooleanField(
        verbose_name="Скрыть запись",
        default=False,
        null=True,
        blank=True,
    )

    # def save(self):
    #     super().save()
    #     city_images = Image.open(self.club_img.path)
    #     if city_images.height > 250 or club_images.width > 200:
    #         output_size = (200, 250)
    #         club_images.thumbnail(output_size)
    #         club_images.save(self.club_img.path)

    def __str__(self):
        return self.country_name

    class Meta:
        verbose_name = "СТРАНА"
        verbose_name_plural = "СТРАНЫ"
