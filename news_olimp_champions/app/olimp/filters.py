import django_filters
from django import forms
from app.olimp.models import Stand, Sportsman, ViewOlimp, ViewSports, Trener, Club, Medal


class StandFilter(django_filters.FilterSet):
    stand_query = Stand.objects.all()
    stand_name = django_filters.CharFilter()
    # stand_description"
    sportsman_id = django_filters.ModelChoiceFilter(queryset=Sportsman.objects.all())
    medal_id = django_filters.ModelChoiceFilter(queryset=Medal.objects.all())
    view_olimp_id = django_filters.ModelChoiceFilter(queryset=ViewOlimp.objects.all())
    # date_event =  django_filters.Model




    class Meta:
        model = Stand
        fields = ["stand_name","view_olimp_id","sportsman_id","medal_id",]
        # exclude = ["book_img"]