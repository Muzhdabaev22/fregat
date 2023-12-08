from django.urls import path
from .views import HomeView, LangView, BlogView, OfertaView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('lang/', LangView.as_view(), name='lang'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('oferta/', OfertaView.as_view(), name='oferta')
]