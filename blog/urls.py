from django.urls import path
from .views import *
urlpatterns = [
    path('ip',get_ip,name="ip ")
]