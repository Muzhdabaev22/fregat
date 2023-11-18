from django.shortcuts import render
from django.views import View
from .forms import FeedBackForm, FeedBackFormSecond
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError

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
        return render(
            request,
            'main/lang.html', context={
                'form': form
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
            

class BlogView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'main/blog.html')