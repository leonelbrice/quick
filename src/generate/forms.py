from dataclasses import fields
from django import forms
from .models import Chapitre,Question

class ChapitreForm(forms.ModelForm):
    class Meta:
        model=Chapitre
        fields=('nom_chapitre',)

class QuestionForm(forms.ModelForm):
  class Meta:
    model=Question
    fields=('intitule','nbre_point','picture','partie','type_question','niveau')



class PartieForm(forms.Form):
      nom_partie=forms.CharField(
        label='nom',
        widget=forms.TextInput(attrs={'class':'form-control'}),
        max_length=100,
        required=True)