# newsapp/urls.py  ← CREATE THIS FILE

from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('sports/', views.sports_view, name='sports'),
    path('business/', views.business_view, name='business'),
    path('entertainment/', views.entertainment_view, name='entertainment'),
    
]
