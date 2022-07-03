#!/usr/bin/wkhtmltopdf
from django.shortcuts import render
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.template.loader import get_template
import pdfkit
from django.template import Context
import os
from wkhtmltopdf.views import PDFTemplateView
from generate.models import *
from auth_user.models import *

def form_all(request):
    if request.user.is_teacher:
        chap=Chapitre.objects.all()
        partie=Partie.objects.all()           
        return JsonResponse({"chapitre":list(chap.values()),"partie":list(partie.values())})


def exercice(request):
    if request.method=="POST":
        chapitre=request.POST['chapitre']
        nom_exercice=request.POST['nom']
        partie=request.POST['partie']
        level=request.POST['level_question']
        type_quest=request.POST['type_question']
        quest=Question.objects.filter(niveau=level,partie_id=partie,type_question=type_quest)
        exerice=Exercice()
        exerice.nom_exercice=nom_exercice
        correcte=Correction()
        for q in quest:
            exerice.contenue=str(exerice.contenue)+"{} {}".format(q.intitule,q.picture)
            cor=Reponse.objects.filter(question=q)
            for c in cor:
                if(c.state==True):
                    correcte.valeur=correcte.valeur+"{}".format(c.valeur)
        cr=Correction.objects.create(valeur=correcte.valeur)
        Exercice.objects.create(
            contenue=exerice.contenue,
            nom_exercice=exerice.nom_exercice,
            correction=cr)
    return viewdata(request)
    
def viewdata(request):
    if request.user.is_teacher:
        assc=Assign.objects.filter(teacher=request.user.teacher)
        context={"assc":assc}
        return render(request,'pdf/epreuve.html',context)

def generate(request,exercice_id):
    exo=Exercice.objects.get(id=exercice_id)
    template = get_template('pdf/generator.html')
    options = {
        'page-size':'Letter',
        'encoding':'UTF-8',
    }  
    context = {"exo": exo}  
    html = template.render(context)  #on retourne le template avec le context
    pdfkit.from_string(html,'out.pdf',options=options)
    pdf = open("out.pdf",encoding="utf8", errors='ignore')
    response = HttpResponse(pdf.read(), content_type='application/pdf')  # Genere la reponse comme reponse pdf.
    response['Content-Disposition'] = 'attachment; filename=output.pdf'
    pdf.close()
    os.remove("out.pdf")  # on supprime le fichier out.pdf du repertoire.
    return response  # retourne la reponse.
    
def download(request):
    all_exercice=Exercice.objects.all()
    context={'all_exercice':all_exercice}
    return render(request,'pdf/generer.html',context)
