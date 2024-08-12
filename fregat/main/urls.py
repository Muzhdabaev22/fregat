from django.urls import path
from .views import HomeView, LangView, BlogView, OfertaView, CinemaView, EpisodeView, get_streaming_video

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('lang/', LangView.as_view(), name='lang'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('oferta/', OfertaView.as_view(), name='oferta'),
    path('cinema/', CinemaView.as_view(), name='cinema'),
    path('cinema/<slug:slug>/', EpisodeView.as_view(), name='episode'),
    path('cinema/stream/<slug:slug>/', get_streaming_video, name='stream'),
]