from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
from django.contrib import messages
from django.utils.html import format_html, format_html_join
from main.forms import FeedBackForm, FeedBackFormSecond 
from main.views import send_mail_first, send_mail_second
from .models import Lessons, Student, Teacher
from .forms import CreateStudentForm, CreateTeacherForm

class AdminSchool(View):
    
    def get(self, request):
         # === forms of communication ===
        form = FeedBackForm() 
        sec_form = FeedBackFormSecond() 
        # ===             ===
        
        return render(request, 'crm/base_admin.html', context={
            'form': form,
            'second_form':sec_form
        })
        
        
    def post(self, request):
         # === processing forms of communication ===
        form = FeedBackForm(request.POST) 
        sec_form = FeedBackFormSecond(request.POST) 
        if 'first' in self.request.POST:
            if form.is_valid():
                name = form.cleaned_data['name']
                social = form.cleaned_data['social']
                if send_mail_first(name, social):
                    return HttpResponseRedirect('/')
            
        if 'second' in self.request.POST:
            if sec_form.is_valid():
                name = sec_form.cleaned_data['name']
                social = sec_form.cleaned_data['social']
                lang = sec_form.cleaned_data['lang']
                if send_mail_second(name, social, lang):
                    return HttpResponseRedirect('/')

                
        return render(request, 'crm/base_admin.html', context={
            'form': form,
            'second_form':sec_form
        })


class TeacherAccount(View):
    
    def get(self, request):
         # === forms of communication ===
        form = FeedBackForm() 
        sec_form = FeedBackFormSecond() 
        # ===             ===


        return render(request, 'crm/base_teacher.html', context={
            'form': form,
            'second_form': sec_form,
            
        })
        
        
    def post(self, request):
         # === processing forms of communication ===
        form = FeedBackForm(request.POST) 
        sec_form = FeedBackFormSecond(request.POST) 
          
        if 'first' in self.request.POST:
            if form.is_valid():
                name = form.cleaned_data['name']
                social = form.cleaned_data['social']
                if send_mail_first(name, social):
                    return HttpResponseRedirect('/')
            
        if 'second' in self.request.POST:
            if sec_form.is_valid():
                name = sec_form.cleaned_data['name']
                social = sec_form.cleaned_data['social']
                lang = sec_form.cleaned_data['lang']
                if send_mail_second(name, social, lang):
                    return HttpResponseRedirect('/')
                
        return render(request, 'crm/teacher.html', context={
            'form': form,
            'second_form':sec_form
        })
        
        
class StudentAccount(View):
    
    def get(self, request):
         # === forms of communication ===
        form = FeedBackForm() 
        sec_form = FeedBackFormSecond() 
        # ===             ===
        
        return render(request, 'crm/student.html', context={
            'form': form,
            'second_form': sec_form, 
        })
        
        
    def post(self, request):
         # === processing forms of communication ===
        form = FeedBackForm(request.POST) 
        sec_form = FeedBackFormSecond(request.POST) 
          
        if 'first' in self.request.POST:
            if form.is_valid():
                name = form.cleaned_data['name']
                social = form.cleaned_data['social']
                if send_mail_first(name, social):
                    return HttpResponseRedirect('/')
            
        if 'second' in self.request.POST:
            if sec_form.is_valid():
                name = sec_form.cleaned_data['name']
                social = sec_form.cleaned_data['social']
                lang = sec_form.cleaned_data['lang']
                if send_mail_second(name, social, lang):
                    return HttpResponseRedirect('/')
                
        return render(request, 'crm/student.html', context={
            'form': form,
            'second_form':sec_form
        })
        
        
        
class LessonsView(View):
    def get(self, request):
        lessons = Lessons.objects.all()
        return render(request, 'crm/block/lessons.html', context={
            'lessons': lessons
        })


class TeachersView(View):
    def get(self, request):
        teachers = Teacher.objects.all()
        return render(request, 'crm/block/teachers.html', context={
            'teachers': teachers
        })   
        

class StudentsView(View):
    def get(self, request):
        students = Student.objects.all()
        return render(request, 'crm/block/students.html', context={
            'students': students
        })


class CreateStudentView(View):
    def get(self, request):
        create_form = CreateStudentForm()
        return render(request, 'crm/block/create_student.html', context={
            "create_form": create_form
        })
        
    def post(self, request):
        create_form = CreateStudentForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            messages.success(request, 'Студент успешно сохранен!')
            status = 'success'
            message = 'Студент успешно сохранен!'
            # Возвращаем пустую форму для очистки
            create_form = CreateStudentForm()
        else:
            status = 'error'
            message = 'Ошибка при сохранении формы.'

        # Рендерим HTML-код формы и сообщений
        html = render_to_string('crm/block/create_student.html', {
            "create_form": create_form
        }, request=request)

        return JsonResponse({
            'status': status,
            'message': message,
            'errors': create_form.errors, 
            'html': html,
        })
        
class CreateTeacherView(View):
    def get(self, request):
        create_form = CreateTeacherForm()
        return render(request, 'crm/block/create_teacher.html', context={
            "create_form": create_form
        })
        
    def post(self, request):
        create_form = CreateTeacherForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            messages.success(request, 'Учитель успешно сохранен!')
            status = 'success'
            message = 'Учитель успешно сохранен!'
            # Возвращаем пустую форму для очистки
            create_form = CreateTeacherForm()
        else:
            status = 'error'
            message = 'Ошибка при сохранении формы.'

        # Рендерим HTML-код формы и сообщений
        html = render_to_string('crm/block/create_teacher.html', {
            "create_form": create_form
        }, request=request)

        return JsonResponse({
            'status': status,
            'message': message,
            'errors': create_form.errors, 
            'html': html,
        })

class MaterialsView(View):
    def get(self, request):
        return render(request, 'crm/block/materials.html', context={
            
        }) 