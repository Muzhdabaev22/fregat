from django import forms


class FeedBackForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'block__form__input',
            'placeholder': "Ваше имя"
        })
    )
    
    tel = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'block__form__input',
            'placeholder': "Ваш номер телефона"
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
            'placeholder': "Ваша соц. сеть VK/TELEGRAM/WHATSAPP"
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