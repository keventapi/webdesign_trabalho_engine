from django.shortcuts import render
from .models import Amuleto, Skill, ArteDoFerrao
# Create your views here.
def index(request):
    return render(request, 'base.html')


def items_habilidades(request):
    amuletos = Amuleto.objects.all()
    skills = Skill.objects.all()
    artes = ArteDoFerrao.objects.all()
    context = {'amuletos': amuletos,
               'skills': skills,
               'artes': artes}
    
    return render(request, "itens_habilidades.html", context)