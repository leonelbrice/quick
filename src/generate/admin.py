from django.contrib import admin

# Register your models here.
from generate.models import *

# Register your models here.
admin.site.register(Chapitre)
admin.site.register(Partie)
admin.site.register(Question)
admin.site.register(Reponse)
admin.site.register(Exercice)
admin.site.register(Correction)