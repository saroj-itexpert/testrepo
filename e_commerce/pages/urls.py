from django.urls import path
# to define path we have to bring path 

from . import views
#from all import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about')
]