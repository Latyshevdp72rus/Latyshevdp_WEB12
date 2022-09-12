from django import forms
from django.contrib.auth.models import User
from django.contrib.admin import widgets
from app.olimp.models import Stand, Sportsman, Trener, Club, FeedBack
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
        widget=forms.TextInput()
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

    class Meta:
        model = Sportsman
        fields = ["sportsman_name", "sportsman_country", "sportsman_birthday", "sportsman_biogrpahy", \
                  "view_sports_id", "trener_id", "sportsman_img"]


class FeedBackForm(forms.Form):
    fb_name = forms.CharField(
        required=True,
        min_length=10,
        max_length=30,
        label="Как к Вам обращаться:",
        # validators=[validation_stand],
        widget=forms.TextInput(attrs={"class": "txt"})
    )
    fb_email = forms.CharField(
        required=True,
        min_length=10,
        max_length=30,
        label="Email для связи:",
        # validators=[validation_stand],
        widget=forms.TextInput(attrs={"class": "txt"})
    )
    fb_message = forms.CharField(
        required=True,
        min_length=10,
        max_length=100,
        label="Ваше сообщение:",
        # validators=[validation_book_name],
        widget=forms.TextInput()
    )

    class Meta:
        model = FeedBack
        fields = ["fb_name", "fb_email", "fb_message"]


class ViewOlimpForm(forms.Form):
    pass


class ViewSportsForm(forms.Form):
    pass


class TrenerForm(forms.Form):
    trener_name = ""
    club_id = ""
    trener_img = ""

    class Meta:
        model = Trener
        fields = ["trener_name", "club_id", "trener_img"]


class ClubForm(forms.Form):
    club_name = forms.CharField(
        required=True,
        min_length=10,
        max_length=30,
        label="Название клуба"
    )
    club_img = ""

    class Meta:
        model = Club
        fields = ["club_name", "club_img"]
