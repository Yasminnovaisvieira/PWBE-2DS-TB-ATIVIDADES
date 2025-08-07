from django.db import models

# Create your models here.

class Autor(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    data_nascimento = models.DateField(null = True, blank = True) # null = True: Pode deixar vazio
    nacion = models.CharField(max_length = 30, null = True, blank = True)
    biografia = models.TextField(null = True, blank = True) 