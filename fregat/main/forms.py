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
    
    tel = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'block__form__input_second',
            'placeholder': "Ваш номер телефона"
        })
    )
    
    comment = forms.CharField(
        max_length=1000, 
        widget=forms.Textarea(
            attrs={
                'class': "comment_form_textarea",
                'placeholder': "Комментарий",
                'rows': "6"
            }
        )
    )     
