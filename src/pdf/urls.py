from django.urls import path
from .views import *

urlpatterns = [
    path('getdata/',form_all,name='form_all'),
    path('viewdata/',viewdata,name='viewdata'),
    path('generator/<int:exercice_id>/',generate,name='generate'),
    path('download/',download,name='download'),
    path('create_exo/',exercice,name='exercice'),
]
