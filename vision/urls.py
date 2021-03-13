from django.urls import path

from . import views

app_name = 'vision'
urlpatterns = [
    # Index path
    path('', views.index, name='index'),
    # Upload path
    path('upload/', views.upload, name='upload'),
]
