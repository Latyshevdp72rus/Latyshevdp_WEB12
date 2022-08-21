from django import forms
from django.contrib.auth.models import User
from django.contrib.admin import widgets


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=20,
        label='Логин',
        widget=forms.TextInput(attrs={"class": "filter"})
    )
    password = forms.CharField(
        max_length=16,
        label='Пароль',
        widget=forms.PasswordInput(attrs={"class": "filter"})
    )

    class Meta:
        models = User
        fields = ('username', 'password')


class RegistrationForm(forms.Form):
    first_name = forms.CharField(
        max_length=250,
        label='Имя: ',
        widget=forms.TextInput(attrs={"class": "filter"})
    )

    last_name = forms.CharField(
        max_length=250,
        label='Фамилия: ',
        widget=forms.TextInput(attrs={"class": "filter"})
    )

    email = forms.EmailField(
        label='Почта: ',
        widget=forms.TextInput(attrs={"class": "filter"})
    )

    username = forms.CharField(
        max_length=20,
        label='Логин: ',
        widget=forms.TextInput(attrs={"class": "filter"})
    )

    password = forms.CharField(
        max_length=16,
        label='Пароль',
        widget=forms.TextInput(attrs={"class": "filter"})
    )
    password2 = forms.CharField(
        max_length=16,
        label='Подтвердите пароль',
        widget=forms.TextInput(attrs={"class": "filter"})
    )

    class Meta:
        model = User

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']
