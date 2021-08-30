from django.urls import path, include
from .views import getListCities, home

urlpatterns = [
    path("list-area",getListCities.as_view(),name='list-area'),
    path("",home,name='home'),
]
