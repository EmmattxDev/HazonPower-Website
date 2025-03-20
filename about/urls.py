# about/urls.py
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import AboutPageView, TeamPageView

app_name = 'about'

urlpatterns = [
    path('', AboutPageView.as_view(), name='about'),
    path('team/', TeamPageView.as_view(), name='team'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)