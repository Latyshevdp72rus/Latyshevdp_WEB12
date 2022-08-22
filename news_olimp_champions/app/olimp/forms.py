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
        label="Заголовок",
        validators=[validation_stand],
        widget=forms.TextInput(),
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

    # date_event
    # sportsman_id
    # view_olimp_id
    # medal_id

    class Meta:
        model = Stand
        fields = ["stand_name", "stand_description", "sportsman_id", "view_olimp_id", "medal_id", "date_event"]