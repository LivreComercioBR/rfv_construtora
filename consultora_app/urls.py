from django.urls import path
from .views import *


urlpatterns = [
    path('homepage', homepage, name='homepage'),
    path('areas_atuacao/', areas_atuacao, name='areas_atuacao'),
    path('area_atuacao/<int:id>/', area_atuacao, name='area_atuacao'),
    path('obras/', obras, name='obras'),
    path('obra/<int:id>/', obra, name='obra'),
    path('clientes/', clientes, name='clientes'),
    path('contato/', contato, name='contato'),
    path('institucional/', institucional, name='institucional'),
]
