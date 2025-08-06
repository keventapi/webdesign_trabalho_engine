from django.shortcuts import render
from .models import Amuleto, Skill, ArteDoFerrao, Chefe, Npc, InimigoComum, MiniChefe, Exploracao, Feitico
# Create your views here.
def index(request):
    return render(request, 'index.html')

def filter_skills(skills):
    skill = ""
    skills_list = []
    for i in skills:
        if i == "\n":
            if len(skill) > 5:
                skill = skill.strip('\r').strip('\n')
                skills_list.append(skill)
            skill = ""
        skill+=i
    return skills_list
    
def items_habilidades(request):
    amuletos = Amuleto.objects.all()
    skills = Skill.objects.all()
    artes = ArteDoFerrao.objects.all()
    feiticos = Feitico.objects.all()
    context = {'amuletos': amuletos,
               'skills': skills,
               'artes': artes,
               'feiticos': feiticos}
    return render(request, "itens_habilidades.html", context)

def mundo(request):
    hornet = Npc.objects.filter(nome="hornet").first()
    palido = Npc.objects.filter(nome="pale king").first()
    sonhadoras = Npc.objects.filter(nome="dreamers").first()
    quirrel = Npc.objects.filter(nome="quirrel").first()
    context = {"personagens": [hornet, palido, sonhadoras, quirrel]}
    return render(request, "mundo.html", context)


def inimigos_chefes(request):
    
    inimigos, chefes, minichefes = InimigoComum.objects.all(), Chefe.objects.all(), MiniChefe.objects.all()
    chefes_detail = []
    for chefe in chefes:
        chefe_skill = filter_skills(chefe.skills)
        chefes_detail.append({"chefe": chefe, "chefe_skills":chefe_skill})
    print(chefes_detail)
    context = {"inimigos": inimigos, "chefes": chefes_detail, "minichefes": minichefes}
    return render(request, "inimigos.html", context)



def exploracao(request):
    mapas_detail = []
    mapas = Exploracao.objects.all()
    for mapa in mapas:
        npcs_list = []
        inimigos_list = []
        npcs = mapa.npcs.all()
        inimigos = mapa.chefes.all()
        for npc in npcs:
            npcs_list.append(npc.nome)
        for inimigo in inimigos:
            inimigos_list.append(inimigo.nome)
        mapas_detail.append({'mapaojc': mapa, 'npc_list': npcs_list, 'inimigos_list': inimigos_list})
    context = {'mapas': mapas_detail}
    return render(request, "exploracao.html", context)