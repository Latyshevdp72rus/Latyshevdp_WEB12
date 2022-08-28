import django_filters
from django import forms
from app.olimp.models import Stand, Sportsman, ViewOlimp, ViewSports, Trener, Club, Medal
from django.contrib.admin import widgets

class StandFilter(django_filters.FilterSet):
    stand_query = Stand.objects.all()
    stand_name = django_filters.ModelChoiceFilter(queryset=Stand.objects.all())


        # django_filters.CharFilter(widget=forms.TextInput(attrs={"class":"txt"}))
    # stand_description"
    sportsman_id = django_filters.ModelChoiceFilter(queryset=Sportsman.objects.all())
    medal_id = django_filters.ModelChoiceFilter(queryset=Medal.objects.all())
    view_olimp_id = django_filters.ModelChoiceFilter(queryset=ViewOlimp.objects.all())
    # date_event =  django_filters.Model

    class Meta:
        model = Stand
        fields = ["stand_name","view_olimp_id","sportsman_id","medal_id",]


class SportsmanFilter(django_filters.FilterSet):
    pass
#     sportsman_query = Stand.objects.all()
#     sportsman_name=django_filters.CharFilter()
#     sportsman_country=django_filters.CharFilter()
#     # sportsman_birthday=''
#     sportsman_biogrpahy=django_filters.CharFilter()
#     view_sports_id= django_filters.ModelChoiceFilter(queryset=ViewOlimp.objects.all())
#     trener_id=django_filters.ModelChoiceFilter(queryset=Trener.objects.all())
#
#     class Meta:
#         model = Stand
#         fields = ["sportsman_name","sportsman_country","sportsman_biogrpahy","view_sports_id",'trener_id']
