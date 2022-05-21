from django.urls import path
from .views import *

app_name = 'front'

urlpatterns = [
    path('', index, name='index'),
]