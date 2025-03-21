# about/urls.py
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'bio'

urlpatterns = [
    path('', views.aboutUs, name='bio'),
    # path('team/', TeamPageView.as_view(), name='team'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)