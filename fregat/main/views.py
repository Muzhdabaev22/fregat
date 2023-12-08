from django.shortcuts import render
from django.views import View
from .forms import FeedBackForm, FeedBackFormSecond
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from main.models import PostBlog
from django.core.paginator import Paginator


class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = FeedBackForm()
        sec_form = FeedBackFormSecond()
        return render(
            request,
            'main/home.html', context={
                'form': form,
                'second_form': sec_form
            }
        )
        
    def post(self, request, *args, **kwargs):
        
        if 'first' in self.request.POST:
            form = FeedBackForm(request.POST)
            sec_form = FeedBackFormSecond(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                tel = form.cleaned_data['tel']
                try:
                    send_mail('С вами хотят связаться!', f"{name}. {tel}", 'edik622mujpc@gmail.com', ['edik622mujpc@gmail.com'])
                except BadHeaderError:
                    return 
                return HttpResponseRedirect('/')
            return render(request, 'main/home.html', context={
                'form': form,
                'second_form': sec_form
            })
            
        if 'second' in self.request.POST:
            form = FeedBackFormSecond(request.POST)
            sec_form = FeedBackFormSecond(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                tel = form.cleaned_data['tel']
                comment = form.cleaned_data['comment']
                try:
                    send_mail('С вами хотят связаться!', f"{name}. {tel}\n{comment}", 'edik622mujpc@gmail.com', ['edik622mujpc@gmail.com'])
                except BadHeaderError:
                    return 
                return HttpResponseRedirect('/')
            return render(request, 'main/home.html', context={
                'form': form,
                'second_form': sec_form
            })
        

class LangView(View):
    def get(self, request, *args, **kwargs):
        form = FeedBackForm()
        sec_form = FeedBackFormSecond()
        return render(
            request,
            'main/lang.html', context={
                'form': form,
                'second_form': sec_form
            }
        )
        
        
    def post(self, request, *args, **kwargs):
        
        if 'first' in self.request.POST:
            form = FeedBackForm(request.POST)
            sec_form = FeedBackFormSecond(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                tel = form.cleaned_data['tel']
                try:
                    send_mail('С вами хотят связаться!', f"{name}. {tel}", 'edik622mujpc@gmail.com', ['edik622mujpc@gmail.com'])
                except BadHeaderError:
                    return 
                return HttpResponseRedirect('/lang')
            return render(request, 'main/lang.html', context={
                'form': form,
                'second_form': sec_form
            })
            
        if 'second' in self.request.POST:
            form = FeedBackFormSecond(request.POST)
            sec_form = FeedBackFormSecond(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                tel = form.cleaned_data['tel']
                comment = form.cleaned_data['comment']
                try:
                    send_mail('С вами хотят связаться!', f"{name}. {tel}\n{comment}", 'edik622mujpc@gmail.com', ['edik622mujpc@gmail.com'])
                except BadHeaderError:
                    return 
                return HttpResponseRedirect('/lang')
            return render(request, 'main/lang.html', context={
                'form': form,
                'second_form': sec_form
            })
            

class BlogView(View):
    def get(self, request, *args, **kwargs):
        form = FeedBackForm()
        sec_form = FeedBackFormSecond()
        posts = PostBlog.objects.all()
        paginator = Paginator(posts, 9)
        
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        return render(request, 'main/blog.html', context={
            # "posts": posts,
            'page_obj': page_obj,
            'form': form,
            'second_form': sec_form
            })
        
    def post(self, request, *args, **kwargs):
        
        if 'first' in self.request.POST:
            form = FeedBackForm(request.POST)
            sec_form = FeedBackFormSecond(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                tel = form.cleaned_data['tel']
                try:
                    send_mail('С вами хотят связаться!', f"{name}. {tel}", 'edik622mujpc@gmail.com', ['edik622mujpc@gmail.com'])
                except BadHeaderError:
                    return 
                return HttpResponseRedirect('/blog')
            return render(request, 'main/blog.html', context={
                'form': form,
                'second_form': sec_form
            })
            
        if 'second' in self.request.POST:
            form = FeedBackFormSecond(request.POST)
            sec_form = FeedBackFormSecond(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                tel = form.cleaned_data['tel']
                comment = form.cleaned_data['comment']
                try:
                    send_mail('С вами хотят связаться!', f"{name}. {tel}\n{comment}", 'edik622mujpc@gmail.com', ['edik622mujpc@gmail.com'])
                except BadHeaderError:
                    return 
                return HttpResponseRedirect('/blog')
            return render(request, 'main/blog.html', context={
                'form': form,
                'second_form': sec_form
            })
            

class OfertaView(View):
    def get(self, request, *args, **kwargs):
        form = FeedBackForm()
        sec_form = FeedBackFormSecond()
        return render(request, 'main/oferta.html', context={
                'form': form,
                'second_form': sec_form
            })


class CinemaView(View):
    def get(self, request, *args, **kwargs):
        form = FeedBackForm
        sec_form = FeedBackFormSecond
        return render(request, 
                'main/cinema.html', context={
                    'form': form,
                    'second_form': sec_form
                })
        