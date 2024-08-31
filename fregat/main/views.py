from django.shortcuts import render
from django.views import View
from .forms import FeedBackForm, FeedBackFormSecond, LevelChoice
from django.http import HttpResponseRedirect, StreamingHttpResponse
from django.core.mail import send_mail, BadHeaderError
from main.models import PostBlog, Movie, Episode, Vocabulary, TestCinema, DiscusBoard, SubStory, RightOrder
from django.core.paginator import Paginator
from .services import open_file
from random import shuffle


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
        
        
        # === processing forms of communication ===
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
            form = FeedBackForm(request.POST)
            sec_form = FeedBackFormSecond(request.POST)
            if sec_form.is_valid():
                name = sec_form.cleaned_data['name']
                social = sec_form.cleaned_data['social']
                lang = sec_form.cleaned_data['lang']
                try:
                    send_mail('С вами хотят связаться!', f"{name}. Социальная сеть: {social}\nЯзык: {lang}", 'edik622mujpc@gmail.com', ['edik622mujpc@gmail.com'])
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
        
        
        # === processing forms of communication ===
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
            form = FeedBackForm(request.POST)
            sec_form = FeedBackFormSecond(request.POST)
            if sec_form.is_valid():
                name = sec_form.cleaned_data['name']
                social = sec_form.cleaned_data['social']
                lang = sec_form.cleaned_data['lang']
                try:
                    send_mail('С вами хотят связаться!', f"{name}. Социальная сеть: {social}\nЯзык: {lang}", 'edik622mujpc@gmail.com', ['edik622mujpc@gmail.com'])
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
        
        # === setting up navigation === 
        posts = PostBlog.objects.all()
        paginator = Paginator(posts, 9)
        
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        # =============================
        
        return render(request, 'main/blog.html', context={
            'page_obj': page_obj,
            'form': form,
            'second_form': sec_form
            })
        
    def post(self, request, *args, **kwargs):
        
        
        # === processing forms of communication ===
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
            form = FeedBackForm(request.POST)
            sec_form = FeedBackFormSecond(request.POST)
            if sec_form.is_valid():
                name = sec_form.cleaned_data['name']
                social = sec_form.cleaned_data['social']
                lang = sec_form.cleaned_data['lang']
                try:
                    send_mail('С вами хотят связаться!', f"{name}. Социальная сеть: {social}\nЯзык: {lang}", 'edik622mujpc@gmail.com', ['edik622mujpc@gmail.com'])
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

    def post(self, request, *args, **kwargs):
        
        
        # === processing forms of communication ===
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
            form = FeedBackForm(request.POST)
            sec_form = FeedBackFormSecond(request.POST)
            if sec_form.is_valid():
                name = sec_form.cleaned_data['name']
                social = sec_form.cleaned_data['social']
                lang = sec_form.cleaned_data['lang']
                try:
                    send_mail('С вами хотят связаться!', f"{name}. Социальная сеть: {social}\nЯзык: {lang}", 'edik622mujpc@gmail.com', ['edik622mujpc@gmail.com'])
                except BadHeaderError:
                    return 
                return HttpResponseRedirect('/oferta')
            return render(request, 'main/lang.html', context={
                'form': form,
                'second_form': sec_form
            })

class CinemaView(View):
    def get(self, request, *args, **kwargs):
        form = FeedBackForm()
        sec_form = FeedBackFormSecond()
        choice_level = LevelChoice()
        
        
        # === we give the selected films using the level ===
        if request.GET.get('lvl'):
            movies_list = Movie.objects.filter(level__level=request.GET.get('lvl'))
            if movies_list:
                return render(request, 
                        'main/cinema.html', context={
                            'form': form,
                            'second_form': sec_form,
                            'movies': movies_list,
                            'choice_level': choice_level
                        })
            else:
                movies_list = Movie.objects.all()
                return render(request, 
                        'main/cinema.html', context={
                            'form': form,
                            'second_form': sec_form,
                            'movies': movies_list,
                            'choice_level': choice_level
                        })
        else:
            movies_list = Movie.objects.all()
            return render(request, 
                    'main/cinema.html', context={
                        'form': form,
                        'second_form': sec_form,
                        'movies': movies_list,
                        'choice_level': choice_level
                    })

    def post(self, request, *args, **kwargs):
        
        
        # === processing forms of communication ===
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
            form = FeedBackForm(request.POST)
            sec_form = FeedBackFormSecond(request.POST)
            if sec_form.is_valid():
                name = sec_form.cleaned_data['name']
                social = sec_form.cleaned_data['social']
                lang = sec_form.cleaned_data['lang']
                try:
                    send_mail('С вами хотят связаться!', f"{name}. Социальная сеть: {social}\nЯзык: {lang}", 'edik622mujpc@gmail.com', ['edik622mujpc@gmail.com'])
                except BadHeaderError:
                    return 
                return HttpResponseRedirect('/')
            return render(request, 'main/home.html', context={
                'form': form,
                'second_form': sec_form
            })
        # =====================================
        
        
        # === we check whether the user has selected the language level ===
        if 'level' in self.request.POST:
            lvl = LevelChoice(request.POST)
            form = FeedBackFormSecond(request.POST)
            sec_form = FeedBackFormSecond(request.POST)
            if lvl.is_valid():
                level = lvl.cleaned_data['level']
                return HttpResponseRedirect(f'?lvl={level}')
            movies_list = Movie.objects.all()
            return render(request, 'main/cinema.html', context={
                'form': form,
                'second_form': sec_form,
                'choice_level': lvl,
                'movies': movies_list
            })


class EpisodeView(View):
    def get(self, request, slug):
        
        # === forms of communication ===
        form = FeedBackForm() 
        sec_form = FeedBackFormSecond() 
        # ===             ===
        
        # === data about episode ===
        movie = Episode.objects.get(url=slug)
        vocabulary = Vocabulary.objects.filter(episode__url=slug)
        test = TestCinema.objects.filter(episode__url=slug)
        discus = DiscusBoard.objects.filter(episode__url=slug)
        story = SubStory.objects.filter(episode__url=slug)
        order = list(RightOrder.objects.filter(episode__url=slug))
        # ==========================
        
        shuffle(order)
        
        return render(request, 'main/episode.html', context={
            'form': form,
            'second_form': sec_form,
            'movie': movie,
            'vocabulary': vocabulary,
            'test': test,
            'discus': discus,
            'story': story,
            "order": order
        })
    
    
    def post(self, request, slug):
        
        # === forms of communication ===
        form = FeedBackForm(request.POST)
        sec_form = FeedBackFormSecond(request.POST)   
        # ===             ===
         
         
        # === data about episode ===     
        movie = Episode.objects.get(url=slug)
        vocabulary = Vocabulary.objects.filter(episode__url=slug)
        test = TestCinema.objects.filter(episode__url=slug)
        discus = DiscusBoard.objects.filter(episode__url=slug)
        story = SubStory.objects.filter(episode__url=slug)
        order = list(RightOrder.objects.filter(episode__url=slug))
        # ==========================
        
        shuffle(order)
        
        # === we check if there are answers to the tests ===    
        if 'test-1' in self.request.POST:
            correct_answers = []
            for key in request.POST.keys():
                if key.startswith("test-"):
                    correct_answers.append(int(request.POST[key]))
                
            return render(request, 'main/episode.html', context={
                'form': form,
                'second_form': sec_form,
                'movie': movie,
                'vocabulary': vocabulary,
                'test': test,
                'answers': correct_answers,
                'discus': discus,
                'story': story,
                "order": order
            })
            
            
        # === processing forms of communication ===
        if 'first' in self.request.POST:
            
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
            form = FeedBackForm(request.POST)
            sec_form = FeedBackFormSecond(request.POST)
            if sec_form.is_valid():
                name = sec_form.cleaned_data['name']
                social = sec_form.cleaned_data['social']
                lang = sec_form.cleaned_data['lang']
                try:
                    send_mail('С вами хотят связаться!', f"{name}. Социальная сеть: {social}\nЯзык: {lang}", 'edik622mujpc@gmail.com', ['edik622mujpc@gmail.com'])
                except BadHeaderError:
                    return 
                return HttpResponseRedirect('/')
            return render(request, 'main/home.html', context={
                'form': form,
                'second_form': sec_form
            })
        # ====================================
            
            
        return render(request, 'main/episode.html', context={
                'form': form,
                'second_form': sec_form,
                'movie': movie,
                'vocabulary': vocabulary,
                'test': test,
            })

def get_streaming_video(request, slug):
    file, status_code, content_length, content_range = open_file(request, slug)
    response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4')

    response['Accept-Ranges'] = 'bytes'
    response['Content-Length'] = str(content_length)
    response['Cache-Control'] = 'no-cache'
    response['Content-Range'] = content_range
    return response