from django.shortcuts import render
from django.views import View


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'main/home.html'
        )
        

class LangView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, 
            'main/lang.html'
        )