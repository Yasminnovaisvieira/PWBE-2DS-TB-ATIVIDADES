# OBEJETIVO: Configura o WSGI do projeto
# WSGI: Padrão para comunicação entre servidores web e aplicações Python

import os # Importa o módulo para interagir com o sistema operacional

from django.core.wsgi import get_wsgi_application # Importa a função que cria o objeto WSGI da aplicação Django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'livraria.settings') # Define a variável de ambiente que aponta para o arquivo de configurações do Django
                                                                     # Isso informa qual configuração o Django deve usar para esse projeto
application = get_wsgi_application() # Cria a aplicação WSGI que o servidor web vai usar para processar requisições
                                     # Essa variável `application` é o ponto de entrada do servidor para o Django