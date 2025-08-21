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
    
class Editora(models.Model):
    editora = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True, null=True, blank=True)
    endereco = models.CharField(max_length=200, null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True) # EmailField = Regras de E-mail
    site = models.URLField(null=True, blank=True) # URLField = 

    def __str__(self):
        return f"{self.editora}"

# blank = True : Não é preciso preencher o campo.
# null = True : Aí se eu deixar vazio, o valor será NULL

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=255)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE) #Pega da tabela Autor
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE) #Pega da tabela editora
    isbn = models.CharField(max_length=255)
    descricao = models.TextField()
    idioma = models.CharField(max_length=255, default="Português")
    ano_publicado = models.IntegerField()
    paginas = models.IntegerField()
    preco = models.DecimalField(max_digits=10,decimal_places=2)
    estoque = models.IntegerField()
    desconto = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel =models.BooleanField(default=True)
    dimensoes = models.CharField(max_length=255)
    peso = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Título: {self.titulo} \n | Autor: {self.autor} \n | Ano: {self.ano_publicado}"