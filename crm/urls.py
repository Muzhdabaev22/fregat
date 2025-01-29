from django.urls import path
from .views import *

app_name = 'crm'

urlpatterns = [
    path('teacher/', TeacherAccount.as_view(), name='teacher'),
    path('student/', StudentAccount.as_view(), name='student'),
    path('adminschool/', AdminSchool.as_view(), name='admin'),
    path('adminschool/lessons/', LessonsView.as_view(), name='lessons'),
    path('adminschool/teachers/', TeachersView.as_view(), name='teachers'),
    path('adminschool/students/', StudentsView.as_view(), name='students'),        
    path('adminschool/create-students/', CreateStudentView.as_view(), name='create_student'),
    path('adminschool/create-teacher/', CreateTeacherView.as_view(), name='create_teacher'),
    path('adminschool/materials/', MaterialsView.as_view(), name='materials'),
]
