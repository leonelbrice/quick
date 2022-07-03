from distutils.log import Log
from django.shortcuts import redirect, render

# Create your views here.
from multiprocessing import context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import *
from auth_user.models import User
from django.template import loader
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required
#cette fonction renvoie la liste des chapitres disponibles dans la base de donnees
def chapitre(request):
    if request.user.is_teacher:
        chapitre_list=[]
        assc=Assign.objects.filter(teacher=request.user.teacher)
        print(assc)
    #on recupere la liste des chapitres  
        query= request.GET.get('query')
        #on recupere la valeur du champ de nom query
        # if not query or query=='':
        #     #on teste si query n'est pas dans la bd ou s'il est vide alors on affiche tout les items
        #     chapitre_list=Chapitre.objects.all()
        #     print(chapitre_list)
        if query:
            for ass in assc:
                ch=Chapitre.objects.filter(ue_id=ass.course.id,nom_chapitre__icontains=query)
                if ch.exists():
                    chapitre_list.append(ch)
                #chapitre_list=Chapitre.objects.filter(nom_chapitre__icontains=query)
                #on utile la classe paginator pour povoir controler l'affichage des elements sur la vue en
        #on definit le nombre d'elements a affiche a 18
        else:
            for ass in assc:
                ch=Chapitre.objects.filter(ue_id=ass.course.id)
                if ch.exists():
                    chapitre_list.append(ch)
        context={'chapitre':chapitre_list,'paginate':True}
        return render(request,"generate/chapitre.html",context)
    return render(request,'auth_user/login.html')
    
@login_required
def partie(request,id_chapitre):
     if request.user.is_teacher:
            query= request.GET.get('query')
            id_chapitre =int(id_chapitre)
            if not query or query=="":
                try:
                    affiche=Partie.objects.filter(chapitre_id=id_chapitre)
                except Partie.DoesNotExist:
                    redirect('/')
            else:
                affiche=Partie.objects.filter(chapitre_id=id_chapitre).filter(nom__icontains=query)
            #partie=["{}".format(i.nom_partie)for i in affiche
            context={'partie':affiche,'query':query,'id_chap':id_chapitre}
            return render(request,'generate/partie.html',context)

@login_required
def del_chap(request,sup):
    if request.user.is_teacher:
        sup=int(sup)
        req=get_object_or_404(Chapitre,pk=sup)
        #req=Chapitre.objects.get(pk=sup)
        try:
            req.delete()
        except Chapitre.DoesNotExist:
            return HttpResponse('Element introuvable')
        return chapitre(request)
    return redirect('accounts/login/')


#cette fonction permet de modifier un chapitre
@login_required
def modif_chap(request,modif):
    if request.user.is_teacher:
        #on recherche le chapitre donc les valeur doivent etre modifier  grace 
        # au parametre modif qui contient id du chapitre en question  
        req=get_object_or_404(Chapitre,pk=modif)
        #on recupere les elements contenues dans le formulaire s'il s'agit de la methode POST
        # sinon on affiche la page de modification des chapitres
        if request.method=='POST':
            modif=int(modif)   
            ue = get_object_or_404(Course, id=request.POST['ue'])
            nom = request.POST['nom']
            image= request.FILES['image']
            desc=request.POST['desc']
            #on modifie les attribut du chapitre en questions
            req.nom_chapitre=nom
            req.desc=desc
            req.image=image
            req.ue=ue
            #on mets a jour la table des chapitres
            req.save()
        assign = Assign.objects.filter(teacher_id=request.user.teacher.id).order_by('-id')
        context = {'assign': assign,'chap':req}
        return render(request,'generate/modif_chapitre.html',context)


@login_required
#on supprime un chapitre
def del_chap(request,sup):
    sup=int(sup)
    req=get_object_or_404(Chapitre,pk=sup)
    #req=Chapitre.objects.get(pk=sup)
    try:
        req.delete()
    except Chapitre.DoesNotExist:
        return HttpResponse('Element introuvable')
    return chapitre(request)

#fonction pour ajouter une partie
@login_required
def add_partie(request,id_chap):
    if request.method=='POST':
        nom=request.POST['nom']
        chap=Chapitre.objects.get(id=id_chap)
        Partie.objects.create(
            nom=nom,
            chapitre=chap
        )
    return render(request,"generate/add_partie.html",{'id_chap':id_chap})
    


@login_required
#affiche les questions lies a une partie
def questionnaire(request,liste):
    partie_id=int(liste)
    requete=Question.objects.filter(partie=partie_id)
    context={'liste':requete,'partie_id':partie_id}
    return render(request,'generate/question.html',context)
    
@login_required
def add_question(request,partie_id):
    context={'partie_id':partie_id}
    if request.method=="POST":
        partie=Partie.objects.get(id=partie_id)
        intitule=request.POST["intitule"]
        Type_question=request.POST['type_question']
        level=request.POST['level_question']
        img=request.FILES['image']
        Question.objects.create(
            intitule=intitule,
            picture=img,
            partie=partie,
            type_question=Type_question,
            niveau=level            
        )    
    return render(request,'generate/add_question.html',context)

@login_required
def rep_onse(request,question_id):
    question=Question.objects.get(id=question_id)
    rep=Reponse.objects.filter(question=question)
    return render(request,'generate/reponse.html',{'question_id':question_id,'all_reponse':rep})

@login_required
def add_reponse(request,question_id):
    if request.method=='POST':
        quest=Question.objects.get(id=question_id)
        valeur=request.POST['valeur']
        state=request.POST['state']
        Reponse.objects.create(
            valeur=valeur,
            state=state,
            question=quest
        )
        return render(request,'generate/reponse.html',{'question_id':question_id})
    return render(request,'generate/add_reponse.html',{'question_id':question_id})    

@login_required()
#permet d'ajouter un chapitre
def add_chap(request):
    if not request.user.is_teacher:
        return redirect("/")
    if request.method == 'POST':
        ue = get_object_or_404(Course, id=request.POST['ue'])
        nom = request.POST['nom']
        image= request.FILES['image']
        desc=request.POST['desc']
        Chapitre(
            nom_chapitre=nom,
            desc=desc,
            image=image,
            ue=ue
        ).save()
        return redirect('chapitre')
    assign = Assign.objects.filter(teacher_id=request.user.teacher.id).order_by('-id')
    context = {'assign': assign }
    return render(request, 'generate/add_chapitre.html', context)

##################Marks###################

@login_required
def del_reponse(request,rep):
    req=get_object_or_404(Reponse,pk=rep)
    #req=Chapitre.objects.get(pk=sup)
    try:
        req.delete()
    except Reponse.DoesNotExist:
        return HttpResponse('Element inexistant')
    return render(request,'generate/reponse.html',{'question_id':req.question.id})

@login_required
def del_question(request,question_id):
    req=get_object_or_404(Question,pk=question_id)
    #req=Chapitre.objects.get(pk=sup)
    try:
        req.delete()
    except Question.DoesNotExist:
        return HttpResponse('Element inexistant')
    return render(request,'generate/question.html',
                  {'question_id':question_id,
                   'partie_id':req.partie.id})
