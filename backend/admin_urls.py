# admin_urls.py
from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', admin.site.urls),
    # path("ckeditor5/", include('django_ckeditor_5.urls')),
    # path('', include('pwa.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)