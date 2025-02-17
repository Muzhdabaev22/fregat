from django import forms
from .models import Student, Teacher, StudentsCode


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['username', 'password', 'name', 'surname', 'city', 'contacts']
    
    password = forms.CharField(
        max_length=200, 
        widget=forms.PasswordInput(attrs={
            "placeholder": "Пароль"
        })
    )
    

class CodeTeacherForm(forms.ModelForm):
    
    teacher = forms.ModelChoiceField(queryset=Teacher.objects.all())
    class Meta:
        model = StudentsCode
        fields = ['code', 'teacher']


class CreateTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['username', 'name']
        
    password = forms.CharField(
        max_length=200, 
        widget=forms.PasswordInput(attrs={
            "placeholder": "Пароль"
        })
    )    
class NoticeLesson(forms.Form):
    date = forms.DateField(
        label="Дата урока",
        required=True,
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'date-input'
        })
    )
    code = forms.CharField(
        max_length=20,
        label="Код ученика",
        widget=forms.TextInput(attrs={
            'placeholder': 'Введите код ученика',
            'autocomplete': 'off'
        })
    )
    cancel_reason = forms.CharField(
        label="",
        required=False,
        widget=forms.Textarea(attrs={
            'placeholder': 'Введите причину отмены',
            'class': 'cancel-reason',
            'style': 'display: none;'  # Скрыто по умолчанию
        })
    )