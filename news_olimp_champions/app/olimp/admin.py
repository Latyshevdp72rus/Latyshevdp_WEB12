from django.contrib import admin
from app.olimp.models import Stand, Sportsman, ViewOlimp, ViewSports, Trener, Club,\
    Medal, FeedBack, CommentsSportsman,Country, CommentsTrener, CommentsStand


class StandAdmin(admin.ModelAdmin):
    """Настройка админки модели Стэнд(Новости)"""
    list_display = ("id", "stand_name", "view_olimp_id", "date_event",
                    "stand_is_visible")
    list_display_links = ("id", "stand_name", "view_olimp_id", "date_event",)
    search_fields = ("stand_name", "view_olimp_id",)
    list_editable = ("stand_is_visible",)
    list_filter = ("stand_name", "date_event",)
    ordering = ("id",)
    fieldsets = (
        ("Основные сведения", {
            "fields": ("stand_name", "stand_description", "date_event","stand_img", "stand_is_visible")
        }),
        ("Прочие сведения", {
            "fields": ("sportsman_id", "view_olimp_id", "medal_id")
        }),
    )


class CommentsStandAdmin(admin.ModelAdmin):
    """Настройка админки модели Блока Стэнд(Новости)"""
    list_display = ("id", "user", "news", "date_created", "moderation_is_visible")
    list_display_links = ("id", "user",)
    search_fields = ("user", "news",)
    list_filter = ("user", "news", "moderation_is_visible",)
    ordering = ("id",)
    fieldsets = (
        ("Основные сведения", {
            "fields": ("user", "news", "text", "moderation_is_visible")
        }),
    )


class SportsmanAdmin(admin.ModelAdmin):
    """Настройка админки модели Спортсмена"""
    list_display = (
        "id", "sportsman_name","sportsman_birthday", "country_id", "view_sports_id","date_created", "sportsman_is_visible")
    list_display_links = ("id", "sportsman_name", "view_sports_id", "sportsman_birthday","country_id",)
    search_fields = ("sportsman_name", "country_id","country_id")
    list_filter = ("sportsman_name", "country_id", "sportsman_is_visible",)
    ordering = ("id",)
    fieldsets = (
        ("Основные сведения", {
            "fields": ("sportsman_name",  "sportsman_birthday","country_id", "sportsman_biogrpahy",
                       "sportsman_img", "sportsman_is_visible")
        }),
        ("Прочие сведения", {
            "fields": ("view_sports_id", "trener_id")
        }),
    )


class CommentsSportsmanAdmin(admin.ModelAdmin):
    """Настройка админки модели Блока комментарий Спортсмена"""
    list_display = ("id", "user", "news", "date_created", "moderation_is_visible")
    list_display_links = ("id", "user",)
    search_fields = ("user", "news",)
    list_filter = ("user", "news", "moderation_is_visible",)
    ordering = ("id",)
    fieldsets = (
        ("Основные сведения", {
            "fields": ("user", "news", "text", "moderation_is_visible")
        }),
    )


class ViewOlimpAdmin(admin.ModelAdmin):
    """Настройка админки модели Виды олимпийских игр"""
    list_display = ("id", "view_olimp_name", "view_olimp_is_visible")
    list_display_links = ("id", "view_olimp_name",)
    search_fields = ("view_olimp_name",)
    list_editable = ("view_olimp_is_visible",)
    list_filter = ("view_olimp_name", "view_olimp_is_visible",)
    ordering = ("id",)
    fieldsets = (
        ("Основные сведения", {
            "fields": ("view_olimp_name", "view_olimp_is_visible",)
        }),
    )


class ViewSportsAdmin(admin.ModelAdmin):
    """Настройка админки модели Виды спорта"""
    list_display = ("id", "view_sport_name", "view_sports_is_visible")
    list_display_links = ("id", "view_sport_name",)
    search_fields = ("view_sport_name",)
    list_editable = ("view_sports_is_visible",)
    list_filter = ("view_sport_name", "view_sports_is_visible",)
    ordering = ("id",)
    fieldsets = (
        ("Основные сведения", {
            "fields": ("view_sport_name", "view_sports_is_visible",)
        }),
    )


class TrenerAdmin(admin.ModelAdmin):
    """Настройка админки модели Тренера"""
    list_display = ("id", "trener_name", "trener_is_visible")
    list_display_links = ("id", "trener_name",)
    search_fields = ("trener_name",)
    list_editable = ("trener_is_visible",)
    list_filter = ("trener_name", "trener_is_visible",)
    ordering = ("id",)
    fieldsets = (
        ("Основные сведения", {
            "fields": ("trener_name", "trener_img", "trener_is_visible",)
        }),
        ("Прочие сведения", {
            "fields": ("club_id",)
        })
    )


class CommentsTrenerAdmin(admin.ModelAdmin):
    """Настройка админки модели Блок комментарий Тренера"""
    list_display = ("id", "user", "news", "date_created", "moderation_is_visible")
    list_display_links = ("id", "user",)
    search_fields = ("user", "news",)
    list_filter = ("user", "news", "moderation_is_visible",)
    ordering = ("id",)
    fieldsets = (
        ("Основные сведения", {
            "fields": ("user", "news", "text", "moderation_is_visible")
        }),
    )


class ClubAdmin(admin.ModelAdmin):
    """Настройка админки модели Клубы"""
    list_display = ("id", "club_name", "club_is_visible")
    list_display_links = ("id", "club_name",)
    search_fields = ("club_name",)
    list_editable = ("club_is_visible",)
    list_filter = ("club_name", "club_is_visible",)
    ordering = ("id",)
    fieldsets = (
        ("Основные сведения", {
            "fields": ("club_name", "club_img", "club_is_visible",)
        }),
    )


class MedalAdmin(admin.ModelAdmin):
    """Настройка админки модели Блок комментарий Тренера"""
    list_display = ("id", "medal_name")
    list_display_links = ("id", "medal_name",)
    search_fields = ("medal_name",)
    list_filter = ("medal_name",)
    ordering = ("id",)
    fieldsets = (
        ("Основные сведения", {
            "fields": ("medal_name",)
        }),
    )


class FeedBackAdmin(admin.ModelAdmin):
    """Настройка админки модели Обратной связи"""
    list_display = ("id", "fb_name", "fb_email")
    list_display_links = ("id", "fb_name",)
    search_fields = ("fb_name", "fb_email",)
    list_filter = ("fb_name", "fb_email",)
    ordering = ("id",)
    fieldsets = (
        ("Основные сведения", {
            "fields": ("fb_name", "fb_email", "fb_message", "fb_img")
        }),
    )


class CountryAdmin(admin.ModelAdmin):
    """Настройка админки модели Страны"""
    list_display = ("id", "country_name", "country_is_visible")
    list_display_links = ("id", "country_name",)
    search_fields = ("country_name",)
    list_editable = ("country_is_visible",)
    list_filter = ("country_name", "country_is_visible",)
    ordering = ("id",)
    fieldsets = (
        ("Основные сведения", {
            "fields": ("country_name", "country_img", "country_is_visible",)
        }),
    )


# Регистрация модели Стэнд(Новости) административной панели
admin.site.register(Stand, StandAdmin)

# Регистрация модели Блок комментарий Стэнд административной панели
admin.site.register(CommentsStand, CommentsStandAdmin)

# Регистрация модели Спортсмена административной панели
admin.site.register(Sportsman, SportsmanAdmin)

# Регистрация модели Блок комментарии спортсмена административной панели
admin.site.register(CommentsSportsman, CommentsSportsmanAdmin)

# Регистрация модели Тренера административной панели
admin.site.register(Trener, TrenerAdmin)

# Регистрация модели Блок Коментарий тренера административной панели
admin.site.register(CommentsTrener, CommentsTrenerAdmin)

# Регистрация модели Виды олимпийских игр административной панели
admin.site.register(ViewOlimp, ViewOlimpAdmin)

# Регистрация модели Виды спорта административной панели
admin.site.register(ViewSports, ViewSportsAdmin)

# Регистрация модели Клубы административной панели
admin.site.register(Club, ClubAdmin)

# Регистрация модели Медалей административной панели
admin.site.register(Medal, MedalAdmin)

# Регистрация модели Обратной связи административной панели
admin.site.register(FeedBack, FeedBackAdmin)

# Регистрация модели Стран административной панели
admin.site.register(Country, CountryAdmin)