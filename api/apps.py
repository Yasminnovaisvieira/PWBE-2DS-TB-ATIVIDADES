# OBJETIVO: Configurar opções básicas do aplicativo Django chamado 'api'
# Registra o app e suas configurações quando o projeto é iniciado

from django.apps import AppConfig # Importa a classe base para configurar um aplicativo Django

# Cria a configuração da aplicação chamada "api"
class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField' # define o tipo padrão de campo para chaves primárias (ID) como BigAutoField
    name = 'api' # Nome do app dentro do projeto (igual ao nome da pasta onde ele está)

# IMPORTANTE: BigAutoField: Inteiro grande, útil para quando a tabela tiver muitos registros