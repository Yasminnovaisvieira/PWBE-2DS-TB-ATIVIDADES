# OBJETIVO: Expor uma endpoint da API que permite listar todos os autores (GET) e criar um autor novo (POST).

from django.shortcuts import render # Importa função para renderizar templates HTML
from rest_framework.generics import ListCreateAPIView # Importa a view genérica que já implementa: GET (lista) e POST (criar)
from .models import Autor # Importa o modelo Autor criado
from .serializers import AutorSerializers # Importa o serializador que converte o Autor em dados JSON e valida dados de entrada
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Cria uam view baseada em classe que permite listar e criar autores via API
class AutoresView(ListCreateAPIView):
    queryset = Autor.objects.all() # Define a fonte de dados (Todos os registros do modelo Autor)
    serializer_class = AutorSerializers # Define o serializador usado para serializar (saída) e desserializar/validar (entrada)

@api_view(['GET', 'POST'])
def visualizacao_autor(request):
    if request.method == 'GET':
        queryset = Autor.objects.all()
        serializer = AutorSerializers(queryset, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AutorSerializers(data = request.data)
        if serializer.save():
            return Response(serializer.data, status = status.HTTP_201_CREATED)
    else:
        return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)

# IMPORTANTE: O serializador é quem traduz objetos Python/Django em formato de dados usados na API (normalmente JSON)
# Serializar: Transforma os dados do banco de dados (objetos) em JSON para enviar na resposta da API
# Desserializar: Receber e validar dados pelo usuário em JSON e converter para objetos Python prontos para salvar no banco
# Decorator: Função que recebe outra função como argumento e estende ou modifica seu comportamento sem alterar diretamente o código da função original