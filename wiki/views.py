from django.shortcuts import render
from .models import Amuleto
# Create your views here.
def index(request):
    return render(request, 'base.html')


def items_habilidades(request):
    amuletos = Amuleto.objects.all()
    context = {'amuletos': amuletos}
    return render(request, "itens_habilidades.html", context)