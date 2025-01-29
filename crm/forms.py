from django import forms
from .models import Student, Teacher
    
    
class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['username', 'name', 'code']
        

    
class CreateTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['username', 'name']