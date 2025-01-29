from django import forms
from django.contrib.auth.forms import AuthenticationForm

class FeedBackForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'block__form__input',
            'placeholder': "Ваше имя"
        })
    )
    
    social = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'block__form__input',
            'placeholder': "Ваша соц. сеть VK/Telegram/Whatsapp"
        })
    )


class FeedBackFormSecond(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'block__form__input_second',
            'placeholder': "Ваше имя"
        })
    )
    
    social = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'block__form__input_second',
            'placeholder': "Ваша соц. сеть VK/Telegram/Whatsapp"
        })
    )
    
    choices_lang = (
        ("-- Все --", 
            (
                ("Английский", "Английский"),
                ("Французский", "Французский"),
                ("Немецкий", "Немецкий"),
                ("Испанский", "Испанский"),
                ("Итальянский", "Итальянский"),
                ("Арабский", "Арабский"),
                ("Китайский", "Китайский"),
                ("Японский", "Японский"),
                ("Корейский", "Корейский"),
                ("Японский", "Японский"),
            )
        ),)

    lang = forms.ChoiceField(choices=choices_lang, label="Выберите язык", required=True, widget=forms.Select(attrs={
        "class": "block__form__input_second"}))


class LevelChoice(forms.Form):
    choices = (
        ("-- Все --", 
            (
                ("A2", "A2"),
                ("B1", "B1"),
                ("B2", "B2"),
            )
        ),)

    level = forms.ChoiceField(choices=choices, label='Выбирете уровень')
    

class SignInForm(AuthenticationForm):
    username = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            "class": "block__form__input_second",
            "placeholder": "Логин"})
        )
    password = forms.CharField(
        max_length=200, 
        widget=forms.PasswordInput(attrs={
            "class": "block__form__input_second",
            "placeholder": "Пароль"
        })
    )

