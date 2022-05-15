from curses import meta
from enum import unique
from django.db import models

# Create your models here.
#classe chapitres qui referencient chaque chapitre
######################################      Chapitre    ###########################################
class Chapitre(models.Model):
    nom_chapitre=models.CharField(max_length=50,unique=True)
    nbre_partie=models.IntegerField(null=True,default=0)
    #fonction __srt__ pour l'affichage de requete  
    def __str__(self):
        return self.nom_chapitre
    
############################################# Partie ###########################################################

class Partie(models.Model):
    nom_partie=models.CharField(max_length=50)
    chapitre=models.ForeignKey(Chapitre,on_delete=models.CASCADE,default=None)

###################################################################################################
class Question(models.Model):
    Type_question=['QRO','QRC','Question_trou','VRAI/FAUX']
    level=['facile','moyen','difficile']
    intitule=models.CharField(max_length=300,unique=True)
    nbre_point=models.IntegerField(default=1)
    picture=models.ImageField()
    date_creation=models.DateTimeField(auto_now_add=True)
    partie=models.ForeignKey(Partie,on_delete=models.PROTECT,default=None)
    type_question=models.CharField(max_length=20,default=Type_question[0])
    niveau=models.CharField(max_length=15,default=level[1])
    def __str__(self):
        return self.intitule

##############################################################################################################

class Reponse(models.Model):
    valeur_rep=models.CharField(max_length=256)
    bonne_rep=models.CharField(max_length=256)
    mauvaise_rep=models.CharField(max_length=256)
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
