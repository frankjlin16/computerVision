from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'vision'
urlpatterns = [
    # Index path
    path('', views.index, name='index'),
    # Upload path
    path('upload/', views.upload, name='upload'),
    # Result path
    path('result/', views.result, name='result')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
