from django import forms
from django.contrib.auth.models import User
from django.contrib.admin import widgets
from app.olimp.models import Stand
from app.olimp.validators import validation_stand


class StandForm(forms.Form):
    stand_name = forms.CharField(
        required=True,
        min_length=10,
        max_length=30,
        label="Заголовок статьи",
        validators=[validation_stand],
        widget=forms.TextInput(attrs={"class": "txt"})
    )
    stand_description = forms.CharField(
        required=True,
        min_length=10,
        max_length=100,
        label="Описание",
        # validators=[validation_book_name],
        widget=forms.TextInput()
    )
    date_event = forms.DateField(
        required=True,
        label="Дата олимпиады",
        # validators=[validation_book_name],
        widget=forms.SelectDateWidget(),
    )
    medal_id = forms.CharField(
        required=True,
        label="Дата олимпиады",
        # validators=[validation_stand],
        widget=forms.TextInput(attrs={"class": "txt"})
    )

    class Meta:
        model = Stand
        fields = ["stand_name", "stand_description", "sportsman_id", "view_olimp_id", "medal_id", "date_event"]


class SportsmanForm(forms.Form):
    sportsman_query = Stand.objects.all()
    sportsman_name = ""
    sportsman_country = ""
    sportsman_birthday = ""
    sportsman_biogrpahy = ""
    view_sports_id = ""
    trener_id = ""
    sportsman_img = ""
    sportsman_is_visible = ""

    class Meta:
        model = Stand
        fields = ["stand_name", "stand_description", "sportsman_id", "view_olimp_id", "medal_id", "date_event"]


class TrenerForm(forms.Form):
    trener_name = ""
    club_id = ""
    trener_img = ""

    class Meta:
        model = Stand
        fields = ["trener_name", "club_id", "trener_img"]
