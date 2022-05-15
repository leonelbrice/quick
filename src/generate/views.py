from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.template import loader
from .forms import ChapitreForm,QuestionForm
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

#cette fonction renvoie la liste des chapitres disponibles dans la base de donnees
def index(request):
    #on recupere la liste des chapitres 
    query= request.GET.get('query')
    #on recupere la valeur du champ de nom query
    if not query or query=='':
        #on teste si query n'est pas dans la bd ou s'il est vide alors on affiche tout les items
        chapitre_list=Chapitre.objects.all()
    else:
        chapitre_list=Chapitre.objects.filter(nom_chapitre__icontains=query)
            #on utile la classe paginator pour povoir controler l'affichage des elements sur la vue en
    #on definit le nombre d'elements a affiche a 18
    paginator=Paginator(chapitre_list,18)
    #on recupere le numero de la page ou l'on se trouve avec la methode GET
    page=request.GET.get('page')
    #on teste l'affichage
    try :
          val1=paginator.page(page)
    #si le numero de page n'est pas un entier on renvoie la 1ere page
    except PageNotAnInteger: 
            val1=paginator.page(1)
    except EmptyPage:
            val1=paginator.page(paginator.num_pages)
    context={'chapitre':val1,'paginate':True} 
    return render(request,"index.html",context)


def partie(request,id_chapitre):
    query= request.GET.get('query')
    id_chapitre =int(id_chapitre)
    if not query or query=="":
        affiche=Partie.objects.filter(chapitre=id_chapitre)
    else:
        affiche=Partie.objects.filter(chapitre__id=id_chapitre).filter(nom_partie__icontains=query)
    partie=["{}".format(i.nom_partie)for i in affiche]
    context={'partie':partie,'query':query,'id_chapitre':id_chapitre}
    return render(request,'partie.html',context)

def create_chap(request):
    form= ChapitreForm(request.POST)
    message=''
    if request.method=='POST':
        try:
            if form.is_valid:
                form.save()
                form=ChapitreForm()
                message="votre chapitre a ete ajoute"
        except ValueError:
            return HttpResponse("ce chapitre existe deja ")
    context={'form':form,'message':message}
    return render(request,'addchap.html',context)

def del_chap(request):
    sup=request.GET.get('supprime')
    req=Chapitre.objects.get(nom_chapitre__icontains=sup)
    try:
        req.delete()
    except Chapitre.DoesNotExist:
        return HttpResponse('Element introuvable')
    return render(request,'index.html')

def form_del_chap(request):
    return render(request,'delchap.html')

def form_question(request):
    form=QuestionForm()
    if request.method=='POST':
        if form.is_valid:
            form.save()
            form=QuestionForm()
    context={'form':form}
    return render(request,'addchap.html',context)