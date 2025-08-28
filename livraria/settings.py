# OBJETIVO: Configura todas as definições essenciais para o funcionamento do projeto Django: caminhos, segurança, apps usados, banco, templates, internacionalização e mais.

from pathlib import Path #Importa a classe Path para lidar com caminhos de arquivos de forma fácil e segura
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent # Define o caminho base do projeto (duas pastas acima deste arquivo) // Usado para referenciar arquivos e diretórios do projeto

SECRET_KEY = 'django-insecure-ax+n8^oybr7f22ld$l!=fp)n3o!c@^^(dx7(d9elle$50tihyi' # Chave secreta do Django, usada para segurança (ex: assinaturas, criptografia) // Nunca deve ser compartilhada publicamente em projetos reais

DEBUG = True # Ativa o modo debug, que mostra erros detalhados e recarrega o servidor automaticamente // Só deve estar True em desenvolvimento, nunca em produção

ALLOWED_HOSTS = [] # Lista de domínios que o Django aceita receber requisições // Vazio significa que aceita só localhost / ambiente de desenvolvimento


# Lista dos aplicativos que o Django deve carregar nesse projeto
INSTALLED_APPS = [
    'django.contrib.admin', # Painel Administrativo
    'django.contrib.auth', # Sistema de autenticação
    'django.contrib.contenttypes', # Suporte a tipos de conteúdos genéricos
    'django.contrib.sessions', # Suporte a sessões (login, cookies)
    'django.contrib.messages', # Sistema de mensagens
    'django.contrib.staticfiles', # Serve arquivos estáticos (CSS, JS)
    'api', # app 'api'
    'rest_framework', # Django REST Framework (API)
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}
 
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

# Lista de middlewares, que processam requisições e respostas
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'livraria.urls' # Define o arquivo principal de rotas do projeto

# Configuração para usar templates HTML no Django // Aqui sem pastas extras de templates, só o padrão dos apps
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'livraria.wsgi.application' # Aponta para o arquivo que cria a aplicação WSGI (ponto de entrada do servidor)


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

# Configura o banco de dados padrão como SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

# Validações para senhas (evitar senhas fracas ou comuns)
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us' # Idioma padrão do projeto

TIME_ZONE = 'UTC' # Fuso horário padrão do projeto

USE_I18N = True # Habilita tradução e localização

USE_TZ = True # Ativa uso de fusos horários para datas e horas


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/' # URL base para servir arquivos estáticos (CSS, JS, imagens)

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField' # Define o tipo padrão de campo para IDs nas tabelas como inteiro grande