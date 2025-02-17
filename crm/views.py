from django.shortcuts import render,redirect
from django.views import View
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib import messages
from .models import Lessons, Student, Teacher, StudentsCode
from .forms import CreateStudentForm, CreateTeacherForm, NoticeLesson, CodeTeacherForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class RoleRequiredMixin(LoginRequiredMixin):
    role_prefix = None

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if not request.user.username.startswith(self.role_prefix):
            raise PermissionDenied("У вас нет доступа к этой странице.")

        return super().dispatch(request, *args, **kwargs)
    
class AdminSchool(RoleRequiredMixin, View):
    role_prefix = 'admin'

    def get(self, request):
        return render(request, 'crm/base_admin.html', context={})

    def post(self, request):
        return render(request, 'crm/base_admin.html', context={})


class TeacherAccount(RoleRequiredMixin, View):
    
    role_prefix = 'teacher'
    
    def get(self, request):
        notice_form = NoticeLesson()
        return render(request, 'crm/base_teacher.html', context={
            'notice_form': notice_form
        })
        
    def post(self, request):
        notice_form = NoticeLesson(request.POST) 
        
        if notice_form.is_valid():
            date = notice_form.cleaned_data['date']
            code = notice_form.cleaned_data['code']
            status = request.POST.get('status')
            reason = notice_form.cleaned_data['cancel_reason']

            # Находим ученика по коду
            try:
                student = Student.objects.get(code=code)
            except Student.DoesNotExist:
                return JsonResponse({'error': 'Ученик не найден'}, status=400)

            # Находим текущего учителя (предположим, что он сохранен в сессии или запросе)
            # teacher = request.user.teacher  # Предполагаем, что учитель связан с пользователем
            
            
            lesson = Lessons(
                date=date,
                status=status,
                reason=reason if status == 'cancaled' else None,
                payed='notpayed'
            )
            
            lesson.save()
            lesson.student.add(student)
            lesson.teacher.add(student.teacher.first())
            

            return JsonResponse({'success': 'Урок успешно отмечен'})
        else:
            return JsonResponse({'errors': notice_form.errors}, status=400)


def get_student_by_code(request):
    code = request.GET.get('code', '')
    if code:
        students = Student.objects.filter(code__startswith=code)
        if students.exists():
            data = {
                'students': [
                    {
                        'name': student.name,
                        'code': student.code,
                        'teachers': [t.name for t in student.teacher.all()]
                    }
                    for student in students
                ]
            }
            return JsonResponse(data)
        else:
            return JsonResponse({'error': 'Ученики не найдены'}, status=404)
    else:
        return JsonResponse({'error': 'Введите код'}, status=400)     
                
        
class StudentAccount(RoleRequiredMixin, View):
    
    role_prefix = 'student'
    
    def get(self, request):

        user = Student.objects.get(username=request.user.username)
        return render(request, 'crm/base_student.html', context={
            "user": user,
        })
        
        
    def post(self, request):               
        return render(request, 'crm/base_student.html', context={
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
        all_codes = StudentsCode.objects.all()
        return render(request, 'crm/block/students.html', {'students': students, 'all_codes': all_codes})
class CreateStudentView(View):
    def get(self, request):
        create_form = CreateStudentForm()
        teacher_and_code_form = CodeTeacherForm()
        return render(request, 'crm/block/create_student.html', {
            "create_form": create_form,
            "code_teacher_form": teacher_and_code_form,
        })

    def post(self, request):
        create_form = CreateStudentForm(request.POST)
        code_teacher_form = CodeTeacherForm(request.POST)

        if create_form.is_valid() and code_teacher_form.is_valid():
            
            student = create_form.save()
            
            code_value = code_teacher_form.cleaned_data.get('code')
            teacher = code_teacher_form.cleaned_data.get('teacher')

            code, _ = StudentsCode.objects.get_or_create(code=code_value)
            code.teacher.add(teacher)
            student.code.add(code)

            password = create_form.cleaned_data['password']
            username = create_form.cleaned_data['username']
            user = User.objects.create_user(
                username=username,
                password=password
            )
            user.save()

            message = 'Студент успешно сохранен!'
            status = 'success'
        else:
            message = 'Ошибка при сохранении формы.'
            status = 'error'

        html = render_to_string('crm/block/create_student.html', {
            "create_form": create_form,
            "code_teacher_form": code_teacher_form,
        }, request=request)

        return JsonResponse({
            'status': status,
            'message': message,
            'errors': create_form.errors.as_json(),
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
            
            password = create_form.cleaned_data['password']
            username = create_form.cleaned_data['username']
            user = User.objects.create_user(
                username=username,
                password=password
            )
            user.save()
            
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

class MaterialsAdminView(View):
    def get(self, request):
        return render(request, 'crm/block/materials_admin.html', context={
            
        }) 

class StudentProfileView(View):
    def get(self, request):
        user = Student.objects.get(username=request.user.username)
        return render(request, 'crm/block/profile.html', context={
            "user": user,
        })   
        
class TicketsStudentView(View):
    def get(self, request):
        return render(request, 'crm/block/student_tickets.html', context={
            
        }) 
        
class MaterialsStudentView(View):
    def get(self, request):
        return render(request, 'crm/block/materials_student.html', context={
            
        })       
        
def logoutUser(request):
    logout(request)
    return redirect('main:home')

class EditStudentView(View):
    def get(self, request, student_id):
        student = get_object_or_404(Student, id=student_id)
        student_data = {
            'id': student.id,
            'name': student.name,
            'surname': student.surname,
            'city': student.city,
            'contacts': student.contacts,
            'start_point': student.start_point,
            'current_point': student.current_point,
            'code': list(student.code.values_list('code', flat=True))
        }
        return JsonResponse({'student': student_data})

    def post(self, request, student_id):
        student = get_object_or_404(Student, id=student_id)
        data = request.POST

        student.name = data.get('name', student.name)
        student.surname = data.get('surname', student.surname)
        student.city = data.get('city', student.city)
        student.contacts = data.get('contacts', student.contacts)
        student.start_point = data.get('start_point', student.start_point)
        student.current_point = data.get('current_point', student.current_point)

        new_codes = data.getlist('code')
        existing_codes = StudentsCode.objects.filter(code__in=new_codes)
        student.code.set(existing_codes)

        student.save()

        updated_data = {
            'id': student.id,
            'name': student.name,
            'surname': student.surname,
            'city': student.city,
            'contacts': student.contacts,
            'start_point': student.start_point,
            'current_point': student.current_point,
            'code': list(student.code.values_list('code', flat=True))
        }
        return JsonResponse({'status': 'success', 'student': updated_data})