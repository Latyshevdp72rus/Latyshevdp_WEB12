from django.contrib import admin
from app.olimp.models import Stand, Sportsman, ViewOlimp, ViewSports, Trener, Club, Medal


class StandAdmin(admin.ModelAdmin):
    pass


class SportsmanAdmin(admin.ModelAdmin):
    pass


class ViewOlimpAdmin(admin.ModelAdmin):
    pass


class ViewSportsAdmin(admin.ModelAdmin):
    list_display = ('id', 'view_sport_name', 'view_sports_is_visible')
    list_display_links = ('id', 'view_sport_name',)
    search_fields = ('view_sport_name',)
    list_editable = ('view_sports_is_visible',)
    list_filter = ('view_sport_name', 'view_sports_is_visible',)
    fieldsets = (
        (None, {
            'fields': ('view_sport_name','view_sports_is_visible',)
        }),
    )


class TrenerAdmin(admin.ModelAdmin):
    list_display = ('id', 'trener_name', 'trener_img', 'trener_is_visible')
    list_display_links = ('id', 'trener_name',)
    search_fields = ('trener_name',)
    list_editable = ('trener_is_visible',)
    list_filter = ('trener_name', 'trener_is_visible',)
    fieldsets = (
        (None, {
            'fields': ('trener_name', 'trener_img' 'trener_is_visible',)
        }),
    )


class ClubAdmin(admin.ModelAdmin):
    list_display = ('id', 'club_name', 'club_img', 'club_is_visible')
    list_display_links = ('id', 'club_name',)
    search_fields = ('club_name',)
    list_editable = ('club_is_visible',)
    list_filter = ('club_name', 'club_is_visible',)
    fieldsets = (
        (None, {
            'fields': ('club_name', 'club_img', 'club_is_visible',)
        }),
    )


class MedalAdmin(admin.ModelAdmin):
    list_display = ('id', 'medal_name', 'medal_is_visible')
    list_display_links = ('id', 'medal_name',)
    search_fields = ('medal_name',)
    list_editable = ('medal_is_visible',)
    list_filter = ('medal_name', 'medal_is_visible',)
    fieldsets = (
        (None, {
            'fields': ('medal_name', 'medal_is_visible',)
        }),
    )


admin.site.register(Stand, StandAdmin)
admin.site.register(Sportsman, SportsmanAdmin)
admin.site.register(ViewOlimp, ViewOlimpAdmin)
admin.site.register(ViewSports, ViewSportsAdmin)
admin.site.register(Trener, TrenerAdmin)
admin.site.register(Club, ClubAdmin)
admin.site.register(Medal, MedalAdmin)
