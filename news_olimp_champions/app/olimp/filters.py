import django_filters
from django import forms
from app.olimp.models import Stand, Sportsman, ViewOlimp, ViewSports, Trener, Club, Medal
from django.contrib.admin import widgets


class StandFilter(django_filters.FilterSet):
    stand_query = Stand.objects.all()
    stand_name = django_filters.ModelChoiceFilter(queryset=Stand.objects.all())
    sportsman_id = django_filters.ModelChoiceFilter(queryset=Sportsman.objects.all())
    medal_id = django_filters.ModelChoiceFilter(queryset=Medal.objects.all())
    view_olimp_id = django_filters.ModelChoiceFilter(queryset=ViewOlimp.objects.all())

    class Meta:
        model = Stand
        fields = ["stand_name", "view_olimp_id", "sportsman_id", "medal_id"]


class SportsmanFilter(django_filters.FilterSet):
    sportsman_query = Sportsman.objects.all()
    sportsman_name = django_filters.ModelChoiceFilter(queryset=Sportsman.objects.all())
    sportsman_country = django_filters.CharFilter()
    trener_id = django_filters.ModelChoiceFilter(queryset=Trener.objects.all())
    view_sports_id = django_filters.ModelChoiceFilter(queryset=ViewSports.objects.all())

    class Meta:
        model = Stand
        fields = ["sportsman_name", "sportsman_country", "trener_id", "view_sports_id"]


class TrenerFilter(django_filters.FilterSet):
    trener_query = Trener.objects.all()
    trener_name = django_filters.CharFilter()
    club_id = django_filters.ModelChoiceFilter(queryset=Club.objects.all())

    class Meta:
        model = Trener
        fields = ["trener_name", "club_id"]

