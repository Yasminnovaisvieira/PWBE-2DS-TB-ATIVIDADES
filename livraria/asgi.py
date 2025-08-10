# OBJETIVO: Configura o ASGI
# ASGI: Padrão moderno para comunicação entre servidores web e aplicações Python, que suporta conexões assíncronas (websockets, etc)

import os # Importa o módulo para interagir com o sistema operacional

from django.core.asgi import get_asgi_application # Importa a função que cria o objeto ASGI da aplicação Django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'livraria.settings') # Define a variável de ambiente para apontar para as configurações do projeto

application = get_asgi_application() # Cria a aplicação ASGI que o servidor vai usar para processar requisições
                                     # Essa variável `application` é o ponto de entrada do servidor para o Django no padrão ASGI