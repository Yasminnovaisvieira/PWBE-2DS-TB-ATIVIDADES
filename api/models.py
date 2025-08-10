# OBJETIVO: Define a estrutura da tabela (Autor) no banco de dados e as regras de cada campo
# Usado para criar, buscar, atualizar e deletar autores

from django.db import models # Importa módulo de modelos do Django // Permite a criação de classes que representam tabelas no banco de dados

# Cria a classe Autor, que será um modelo no Django, e cada atributo será uma coluna no banco de dados
class Autor(models.Model):
    nome = models.CharField(max_length=255) # Campo de texto (String) // 'max_length=255': Define o limite máximo de caracteres
    sobrenome = models.CharField(max_length=255) # Campo de texto (String) // 'max_length=255': Define o limite máximo de caracteres
    data_nascimento = models.DateField(null=True, blank=True) # Datas (ano-mês-dia) // 'null=True': Pode ficar vazio no banco // 'blank=True': Pode ficar vazio nos formulários/validações
    nacao = models.CharField(max_length=30, null=True, blank=True) # Até 30 caracteres // Também pode ser deixado em branco ou nulo
    biografia = models.TextField(null=True, blank=True) # Pode ser vazio ou nulo

    # Método que define como o objeto será exibido como string
    # Usado no admin, shell e logs
    def __str__(self):
        return f"{self.nome} {self.sobrenome}" # Retorna o nome completo do autor