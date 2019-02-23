from django.urls import path
# to define path we have to bring path 

from . import views
#from all import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
]