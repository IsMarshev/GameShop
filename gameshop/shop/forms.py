from django import forms
from django.core.validators import RegexValidator
from django.forms import DateInput


class UserForm(forms.Form):
        username = forms.CharField(label='Никнейм', max_length=20, min_length=2, error_messages={
            'max_length': 'Максимальное количество символов - 20',
            'min_length': 'Минимальное количество символов - 3',
            'required': 'Это поле является обязательным'

        })
        age = forms.DateField(label='Возраст', widget=DateInput(attrs={'type': 'date'}), error_messages={
        'required': 'Это поле является обязательным'
        })
        email = forms.CharField(label='Почта', max_length=40, min_length=10, error_messages={
            'max_length': 'Максимальное количество символов - 40',
            'min_length': 'Минимальное количество символов - 10',
            'required': 'Это поле является обязательным'

        })
        telephone = forms.CharField(label='Номер телефона', max_length=10, min_length=10, error_messages={
            'max_length': 'Максимальное количество символов - 10',
            'min_length': 'Минимальное количество символов - 10',
            'required': 'Это поле является обязательным'

        })
        password = forms.CharField(label='Пароль', max_length=20, min_length=8, error_messages={
            'max_length': 'Максимальное количество символов - 20',
            'min_length': 'Минимальное количество символов - 8',
            'required': 'Это поле является обязательным'
        })


class LoginForm(forms.Form):
    username = forms.CharField(label='Никнейм', max_length=100)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())

