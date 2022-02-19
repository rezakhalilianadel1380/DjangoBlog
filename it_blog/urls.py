from django import urls
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import contact_us, custom, homepage
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage,name='homepage'),
    path('contact_us',contact_us,name='contact_us'),
    path('',include('nlg_article.urls')),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('admir/',custom),
    path('djga/', include('google_analytics.urls')),
    
    
  
    
]

if settings.DEBUG:
    urlpatterns =urlpatterns+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns =urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
