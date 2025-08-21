# OBJETIVO: Definir as rotas da API que vão chamar as views corretas.

from django.urls import path # Importa a função 'path' para definir rotas da aplicação
from .views import * # Importa todo o conteúdo do arquivo 'views.py' // Puxa o 'AutoresView'
from .views import visualizacao_autor, EditorasView, LivrosView # Ou colocar * para importar tudo

# Lista as rotas de aplicação
urlpatterns = [
    path('autores', AutoresView.as_view()), #Cria a rota '/autores' e quando o usuário acessar, a view 'AutoresView' será chamada
    # '.as_view()' = Transforma a classe em uma função que o Django consegue usar
    path('authors', visualizacao_autor),
    path('editoras', EditorasView.as_view())
]

# IMPORTANTE: Normalmente se adiciona uma barra no final ('autores/') para seguir o padrão REST do Django
# REST: Estilo de arquitetura para criar APIs que seguem algumas regras e padrões para comunicação entre cliente e servidor

