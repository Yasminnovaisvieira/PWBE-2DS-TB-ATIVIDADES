# OBJETIVO: Definir como os dados do modelo (Autor, nesse caso) serão convertidos para JSON quando enviados na resposta da API e como o JSON recebido será convertido/validado antes de virae um objeto (Autor) salvo no banco de dados

from rest_framework import serializers # Importa o módulo de serializadores do Django REST Framework
                                       # Ele fornece classes e funções para converter dados Python para JSON (vice-versa também) e validar dados
from .models import Autor # Improta o modelo Autor, que representa a tabela no banco e os campos dela

# Cria uma classe de serialzação baseada no ModelSerializer
# ModelSerializer: Cria os campos automaticamente a partir de um modelo Django
class AutorSerializers(serializers.ModelSerializer):
    # Configurações do serializador
    class Meta:
        model = Autor # Diz qual modelo do Django será usado como base (Autor)
        fields = '__all__' # Indica que todos os campos do modelo devem ser incluídos no serializador