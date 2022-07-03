from django.contrib import admin
from django.urls import path,re_path
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^Chapitre/$',chapitre,name='chapitre'),
    re_path(r'^Partie/(?P<liste>[0-9]+)/$',questionnaire,name='questionnaire'),
    path('Partie/<int:id_chap>/add',add_partie,name="add_partie"),
    path('Question/<int:partie_id>/add',add_question,name='add_question'),
    path('Question/<int:question_id>/del',del_question,name='del_question'),
    path('Reponse/<int:question_id>/',rep_onse,name='reponse'),
    path('Reponse/<int:question_id>/add',add_reponse,name='add_reponse'),
    path('Reponse/<int:rep>/del',del_reponse,name='del_reponse'),
    re_path(r'^Chapitre/(?P<id_chapitre>[0-9]+)/$',partie,name='partie'),
    re_path(r'^Chapitre/add/$',add_chap,name="add_chap"),
    re_path(r'^Chapitre/del/(?P<sup>[0-9]+)/$',del_chap,name='del_chap'),
    re_path(r'^Chapitre/mod/(?P<modif>[0-9]+)/$',modif_chap,name='modif_chap'),
]