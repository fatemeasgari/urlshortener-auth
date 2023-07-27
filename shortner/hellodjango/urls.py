from . import views
from django.urls import path

urlpatterns = [
    path('', views.hello),
#    path('get', views.echo)
    path('post', views.echo)
]
