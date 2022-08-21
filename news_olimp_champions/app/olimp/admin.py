from django.contrib import admin
from app.olimp.models import Stand, Sportsman, ViewOlimp, ViewSports, Trener, Club, Medal


class StandAdmin(admin.ModelAdmin):
    list_display = ("id", "stand_name", "view_olimp_id", "date_event",
                    "stand_is_visible")
    list_display_links = ("id", "stand_name", "view_olimp_id", "date_event",)
    search_fields = ("stand_name", "view_olimp_id",)
    list_editable = ("stand_is_visible",)
    list_filter = ("stand_name", "date_event",)
    ordering = ("id",)
    fieldsets = (
        ("Основные сведения", {
            "fields": ("stand_name", "stand_description", "date_event", "stand_is_visible")
        }),
        ("Прочие сведения", {
            "fields": ("sportsman_id", "view_olimp_id", "medal_id")
        }),
    )


# "sportsman_biogrpahy", "view_sports_id", "trener_id", "sportsman_img",
class SportsmanAdmin(admin.ModelAdmin):
    list_display = (
        "id", "sportsman_name", "sportsman_country", "sportsman_birthday", "view_sports_id", "sportsman_is_visible")
    list_display_links = ("id", "sportsman_name", "view_sports_id", "sportsman_birthday", "sportsman_country",)
    search_fields = ("sportsman_name", "sportsman_country",)
    list_editable = ("sportsman_is_visible",)
    list_filter = ("sportsman_name", "sportsman_country", "sportsman_is_visible",)
    ordering = ("id",)
    fieldsets = (
        ("Основные сведения", {
            "fields": ("sportsman_name", "sportsman_country", "sportsman_birthday", "sportsman_biogrpahy",
                       "sportsman_img", "sportsman_is_visible")
        }),
        ("Прочие сведения", {
            "fields": ("view_sports_id", "trener_id")
        }),
    )


class ViewOlimpAdmin(admin.ModelAdmin):
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


class ClubAdmin(admin.ModelAdmin):
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
    list_display = ("id", "medal_name", "medal_is_visible")
    list_display_links = ("id", "medal_name",)
    search_fields = ("medal_name",)
    list_editable = ("medal_is_visible",)
    list_filter = ("medal_name", "medal_is_visible",)
    ordering = ("id",)
    fieldsets = (
        ("Основные сведения", {
            "fields": ("medal_name", "medal_is_visible",)
        }),
    )


admin.site.register(Stand, StandAdmin)
admin.site.register(Sportsman, SportsmanAdmin)
admin.site.register(ViewOlimp, ViewOlimpAdmin)
admin.site.register(ViewSports, ViewSportsAdmin)
admin.site.register(Trener, TrenerAdmin)
admin.site.register(Club, ClubAdmin)
admin.site.register(Medal, MedalAdmin)
