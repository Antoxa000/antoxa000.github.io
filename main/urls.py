from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='task'),
    path('main', views.about, name='main'),
    path('maketask', views.maketask, name='maketask'),
    path('another', views.another, name='another')
]
