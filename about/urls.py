# about/urls.py
from django.urls import path
from .views import AboutPageView, TeamPageView

urlpatterns = [
    path('', AboutPageView.as_view(), name='about'),
    path('team/', TeamPageView.as_view(), name='team'),
]