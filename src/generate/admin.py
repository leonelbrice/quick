from django.contrib import admin

from generate.models import Chapitre, Partie, Question, Reponse

# Register your models here.
admin.site.register(Chapitre)
admin.site.register(Partie)
admin.site.register(Question)
admin.site.register(Reponse)
