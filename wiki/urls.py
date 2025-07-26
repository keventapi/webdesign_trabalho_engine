from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('items', views.items_habilidades),
    path('mundo', views.mundo),
    path('inimigos', views.inimigos_chefes),
    path('exploracao', views.exploracao)
]