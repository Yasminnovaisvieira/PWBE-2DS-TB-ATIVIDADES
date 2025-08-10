# OBJETIVO: Definir as rotas globais do projeto // Ele conecta o painel admin e encaminha as requisições que começar com /api/ para as rotas específicas do app 'api'

from django.contrib import admin # Importa as rotas do painel administrativo do Django
from django.urls import path, include # Importa as funções para criar rotas (`path`) e incluir outras rotas (`include`)

# Lista principal de rotas do projeto Django
urlpatterns = [
    path('admin/', admin.site.urls), # Mapeia a URL /admin/ para o painel administrativo padrão do Django
    path('api/', include('api.urls')) # Inclui todas as rotas que estão no arquivo 'urls.py' do app 'api'
                                      # Ou seja, todas as URLs da api estarão dentro do caminho /api/
]