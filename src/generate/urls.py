from django.urls import include,re_path
from . import views
urlpatterns = [
    re_path(r'^$',views.index,name='index'),
    re_path(r'^Chapitre/(?P<id_chapitre>[0-9]+)/$',views.partie,name='partie'),
    re_path(r'^Chapitre/add/$',views.create_chap,name='create_chap'),
    re_path(r'^Chapitre/form_del/$',views.form_del_chap,name='form_del_chap'),
    re_path(r'^Chapitre/del/$',views.del_chap,name='del_chap'),
    re_path(r'^Question/$',views.form_question,name='form_question'),
]
