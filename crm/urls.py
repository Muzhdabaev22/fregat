from django.urls import path
from .views import *

app_name = 'crm'

urlpatterns = [
    path('teacher/', TeacherAccount.as_view(), name='teacher'),
    path('teacher/get-student/', get_student_by_code, name='get_student'), 
    path('student/', StudentAccount.as_view(), name='student'),
    path('student/profile', StudentProfileView.as_view(), name='student_profile'),
    path('student/tickets', TicketsStudentView.as_view(), name='student_tickets'),
    path("student/materials", MaterialsStudentView.as_view(), name="student_materials"),
    path('adminschool/', AdminSchool.as_view(), name='admin'),
    path('adminschool/lessons/', LessonsView.as_view(), name='lessons'),
    path('adminschool/teachers/', TeachersView.as_view(), name='teachers'),
    path('adminschool/students/', StudentsView.as_view(), name='students'), 
    path('adminschool/students/<int:student_id>/', EditStudentView.as_view(), name='edit_student'),       
    path('adminschool/create-students/', CreateStudentView.as_view(), name='create_student'),
    path('adminschool/create-teacher/', CreateTeacherView.as_view(), name='create_teacher'),
    path('adminschool/materials/', MaterialsAdminView.as_view(), name='materials_admin'),
    path('logout/', logoutUser, name='logout'),
]
