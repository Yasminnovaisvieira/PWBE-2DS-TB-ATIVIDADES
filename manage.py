#!/usr/bin/env python --> Indica que esse arquivo deve ser executado com o interpretador Python do sistema

# OBJETIVO: Porta de entrada para executar comandos do Django pelo terminal // Serve para iniciar o servidor de desenvolvimento, criar migrações, rodar testes, e muito mais
# Esse arquivo é a ferramenta de linha de comando do Django

import os # Importa o módulo para interagir com o sistema operacional
import sys # Importa o módulo para interagir com argumentos de linha de comando


# Função principal que roda comandos administrativos do Django
def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'livraria.settings') # Define a variável de ambiente para apontar para as configurações do projeto // Isso é necessário para o Django saber qual projeto usar

    try:
        from django.core.management import execute_from_command_line # Importa a função que executa comandos do Django passados via terminal
    except ImportError as exc:
        # Se não encontrar Django instalado, lança erro explicando o problema
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    execute_from_command_line(sys.argv) # Executa o comando passado no terminal
                                        # Por exemplo: python manage.py runserver: Inicia o servidor // python manage.py migrate: Aplica migrações no banco

# Executa a função main() só se o arquivo for rodado diretamente (não importado)
if __name__ == '__main__':
    main()
