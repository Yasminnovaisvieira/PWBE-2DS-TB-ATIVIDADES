# OBJETIVO: Registra os modelos no painel administrativo do Django, permitindo o gerenciamento dos dados pelo site '/admin' sem precisar criar telas personalizadas

from django.contrib import admin # Importa as ferramentas do Django para gerenciar o painel administrativo
from .models import * # Importa todos os modelos do arquivo models.py da mesma pasta (Autor)

admin.site.register(Autor) # Registra o modelo Autor no painel admin do Django // Isso permite criar, editar, listar e excluir autores direto pelo admin
admin.site.register(Editora)
admin.site.register(Livro)