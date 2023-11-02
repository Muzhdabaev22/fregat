from django.urls import path
from .views import HomeView, LangView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('lang/', LangView.as_view(), name='lang')
]