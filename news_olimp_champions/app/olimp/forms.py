from django import forms
from app.olimp.models import Stand, Sportsman, Trener, FeedBack, CommentsSportsman, CommentsTrener
from app.olimp.validators import validation_stand

class DateTimeInput(forms.DateTimeInput):
    input_type = 'date'


class StandForm(forms.Form):
    class Meta:
        model = Stand
        fields = ["stand_name", "stand_description", "sportsman_id", "view_olimp_id", "medal_id", "date_event","stand_img"]



class SportsmanForm(forms.Form):
    sportsman_birthday = forms.DateField(widget=DateTimeInput())


    class Meta:
        model = Sportsman
        fields = ["sportsman_name", "country_id", "sportsman_birthday", "sportsman_biogrpahy", "view_sports_id", "trener_id", "sportsman_img"]


class CommentsSportsmanForm(forms.ModelForm):
    class Meta:
        model = CommentsSportsman
        fields = ['text', ]


class TrenerForm(forms.Form):
    class Meta:
        model = Trener
        fields = ["trener_name", "club_id", "trener_img"]


class CommentsTrenerForm(forms.ModelForm):
    class Meta:
        model = CommentsTrener
        fields = ['text', ]

class FeedBackForm(forms.Form):
    class Meta:
        model = FeedBack
        fields = ["fb_name", "fb_email", "fb_message", "fb_img"]
