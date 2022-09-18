import django_filters
from django import forms
from django.forms import DateTimeInput

from app.olimp.models import Stand, Sportsman, ViewOlimp, ViewSports, Trener, Club, Medal
from django.contrib.admin import widgets


class DateTimeInput(forms.DateTimeInput):
    input_type = 'date'


class StandFilter(django_filters.FilterSet):
    stand_query = Stand.objects.all()
    stand_name = django_filters.ModelChoiceFilter(queryset=Stand.objects.all())
    sportsman_id = django_filters.ModelChoiceFilter(queryset=Sportsman.objects.all())
    medal_id = django_filters.ModelChoiceFilter(queryset=Medal.objects.all())
    view_olimp_id = django_filters.ModelChoiceFilter(queryset=ViewOlimp.objects.all())
    date_event = django_filters.DateFilter(
        label=('Дата олимпиады'),
        lookup_expr=('icontains'),
        widget=DateTimeInput()
    )

    class Meta:
        model = Stand
        fields = ["stand_name", "sportsman_id", "medal_id", "view_olimp_id", "date_event"]


class SportsmanFilter(django_filters.FilterSet):
    sportsman_query = Sportsman.objects.all()
    sportsman_name = django_filters.ModelChoiceFilter(queryset=Sportsman.objects.all())
    sportsman_birthday = django_filters.DateFilter(
        label=('Дата Рождения'),
        lookup_expr=('icontains'),
        widget=DateTimeInput()
    )
    sportsman_country = django_filters.CharFilter()
    view_sports_id = django_filters.ModelChoiceFilter(queryset=ViewSports.objects.all())
    trener_id = django_filters.ModelChoiceFilter(queryset=Trener.objects.all())

    class Meta:
        model = Stand
        fields = ["sportsman_name", "sportsman_country", 'sportsman_birthday', "view_sports_id", "sportsman_country", "trener_id"]


class TrenerFilter(django_filters.FilterSet):
    trener_query = Trener.objects.all()
    trener_name = django_filters.CharFilter()
    club_id = django_filters.ModelChoiceFilter(queryset=Club.objects.all())

    class Meta:
        model = Trener
        fields = ["trener_name", "club_id"]
