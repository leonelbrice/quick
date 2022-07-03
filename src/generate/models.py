from distutils.command.upload import upload
from django.db import models

# Create your models here.

from auth_user.models import *

type_epreuve=(
              ('Controle continu','CC'),
              ('Session Normal','SN')
              )

Type_question=(('QRO','QRO'),('QRC','QRC'),
                ('Question_trou','Question_trou'),
                ('VRAI/FAUX','VRAI/FAUX'),)

level=(('facile','facile'),
        ('moyen','moyen'),
        ('difficile','difficile'),)

class Chapitre(models.Model):
    nom_chapitre=models.CharField(max_length=50,unique=True)
    desc=models.TextField(max_length=50,null=True,blank=False)
    image=models.ImageField(null=True,blank=True)
    ue=models.ForeignKey(Course,on_delete=models.CASCADE)
    #fonction __srt__ pour l'affichage de requete  
    def __str__(self):
        return self.nom_chapitre
    
############################################# Partie ###########################################################

class Partie(models.Model):
    nom=models.CharField(max_length=50)
    chapitre=models.ForeignKey(Chapitre,on_delete=models.CASCADE,default=None)
    def __str__(self):
        return self.nom
    
    #def nbre_question(self):

###################################################################################################
class Question(models.Model):
    intitule=models.TextField()
    picture=models.ImageField(null=True,blank=True)
    date_creation=models.DateTimeField(auto_now_add=True)
    partie=models.ForeignKey(Partie,on_delete=models.CASCADE)
    type_question=models.CharField(max_length=20,null=True,choices=Type_question)
    niveau=models.CharField(max_length=200,choices=level,null=False)
    def __str__(self): 
        return self.intitule

##############################################################################################################

class Reponse(models.Model):
    valeur=models.CharField(max_length=256)
    state=models.BooleanField(default=True)
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    def __str__(self):
        return self.valeur
######################################################################################
class Correction(models.Model):
    valeur=models.TextField(max_length=10000)


class Epreuve(models.Model):    
    nom_epreuve=models.CharField(max_length=25,null=False)
    contenue=models.TextField(default=1)
    type_epreuve=models.CharField(max_length=25,choices=type_epreuve)
    annee=models.DateField(auto_now_add=True)
    correction=models.ManyToManyField(Correction,related_name="epreuve")
    
class Exercice(models.Model):    
    nom_exercice=models.CharField(max_length=25,null=False)
    contenue=models.TextField(default=1)
    create_at=models.DateField(auto_now_add=True)
    correction=models.OneToOneField(Correction,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nom_exercice