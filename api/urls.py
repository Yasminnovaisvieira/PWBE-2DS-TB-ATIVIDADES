# OBJETIVO: Definir as rotas da API que vão chamar as views corretas.

from django.urls import path # Importa a função 'path' para definir rotas da aplicação
from .views import * # Importa todo o conteúdo do arquivo 'views.py' // Puxa o 'AutoresView'
from .views import visualizacao_autor, EditorasView, LivrosView, AutoresDetailView, EditorasDetailView, LivrosDetailView  # Ou colocar * para importar tudo
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import permissions

# Lista as rotas de aplicação
urlpatterns = [
    # GET / POST
    path('autores/', AutoresView.as_view()),
    path('authors/', visualizacao_autor),
    path('editoras/', EditorasView.as_view()),
    path('livros/', LivrosView.as_view()),

    # UPDATE / DELETE
    path('autor/<int:pk>/', AutoresDetailView.as_view()),
    path('editora/<int:pk>/', EditorasDetailView.as_view()),
    path('livro/<int:pk>/', LivrosDetailView.as_view()),

    # JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]