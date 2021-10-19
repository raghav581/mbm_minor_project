from django.urls import path, include
from .views import getListCities, home, predictPrice

urlpatterns = [
    path("get-location",getListCities.as_view(),name='list-area'),
    path("predict-price",predictPrice.as_view(),name='predict-price'),
    
    path("",home,name='home'),
]
