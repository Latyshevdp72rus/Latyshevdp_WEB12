from django import forms
from django.contrib.auth.models import User
from django.contrib.admin import widgets
from django import forms
from app.olimp.models import Stand, Sportsman, Trener, Club, FeedBack, ViewOlimp,Medal,CommentsSportsman
from app.olimp.validators import validation_stand


class CommentsForm(forms.ModelForm):
    class Meta:
        model = CommentsSportsman
        fields=['text',]

# validators=[validation_book_name],
class DateTimeInput(forms.DateTimeInput):
    input_type = 'date'


class StandForm(forms.Form):
    stand_name = forms.CharField(
        required=True,
        min_length=10,
        max_length=30,
        label="Заголовок статьи",
        validators=[validation_stand],
        widget=forms.TextInput()
    )
    stand_description = forms.CharField(
        required=True,
        min_length=10,
        max_length=100,
        label="Описание",
        widget=forms.TextInput()
    )
    sportsman_id = forms.SelectMultiple(

    )
    view_olimp_id = forms.SelectMultiple(

    )
    medal_id = forms.SelectMultiple(

    )
    date_event = forms.DateField(
        required=True,
        label="Дата олимпиады",
        widget=DateTimeInput(),
    )

    class Meta:
        model = Stand
        fields = ["stand_name", "stand_description", "sportsman_id", "view_olimp_id", "medal_id", "date_event"]


class SportsmanForm(forms.Form):
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
        widget=forms.TextInput()
    )
    fb_email = forms.CharField(
        required=True,
        min_length=10,
        max_length=30,
        label="Email для связи:",
        widget=forms.TextInput()
    )
    fb_message = forms.CharField(
        required=True,
        min_length=10,
        max_length=100,
        label="Ваше сообщение:",
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
