from django.contrib import admin
from .models import (
    Chefe,
    Npc,
    Exploracao,
    Amuleto,
    Mascara,
    Recipiente,
    PaleOre,
    Feitico,
    ArteDoFerrao,
)

admin.site.register(Chefe)
admin.site.register(Npc)
admin.site.register(Exploracao)
admin.site.register(Amuleto)
admin.site.register(Mascara)
admin.site.register(Recipiente)
admin.site.register(PaleOre)
admin.site.register(Feitico)
admin.site.register(ArteDoFerrao)
