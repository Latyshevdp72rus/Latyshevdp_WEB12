import django_filters
from django import forms
from app.olimp.models import Stand, Sportsman, ViewOlimp, ViewSports, Trener, Club, Medal


class StandFilter(django_filters.FilterSet):
    stand_query = Stand.objects.all()
    stand_name = django_filters.CharFilter()
    # sportsman_id = django_filters.ModelChoiceFilter()

    # date_event = django_filters.ModelChoiceFilter(queryset=Stand.objects.all())

    class Meta:
        model = Stand
        fields = ['stand_name']
        # exclude = ['book_img']