from django.db import models

# Create your models here.
class Stand(models.Model):
    localizacao= models.CharField(max_length=200)
    valor = models.FloatField()

class Reserva(models.Model):
    cnpj = models.CharField(max_length=200)
    nome_empresa = models.CharField(max_length=200)
    categoria_empresa = models.CharField(max_length=200)
    quitado = models.BooleanField()
    standes = models.ForeignKey(Stand,on_delete=models.CASCADE)