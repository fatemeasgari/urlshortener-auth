from django.urls import path
from . import views

urlpatterns = [
    path('', views.links, name='links'),
    path('get', views.echo, name='get'),
]
