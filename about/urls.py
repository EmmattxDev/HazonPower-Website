# about/urls.py
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from .views import aboutUs

app_name = 'about'

urlpatterns = [
    path('', aboutUs, name='about'),
    # path('team/', TeamPageView.as_view(), name='team'),
    path("__reload__/", include("django_browser_reload.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)