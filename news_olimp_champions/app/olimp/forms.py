from django import forms
from django.contrib.auth.models import User
from django.contrib.admin import widgets
from app.olimp.models import Stand
# from app.olimp.validators import validation_book_name


class StandForm(forms.Form):
    pass
    # stand_name = forms.CharField(
    #     required=True,
    #     min_length=4,
    #     label='Название книги',
    #     # validators=[validation_book_name],
    #     widget=forms.TextInput()
    # # attrs = {"class": "librarys_text"}
    # )
    # stand_description
    # sportsman_id
    # view_olimp_id
    # medal_id
    # date_event
