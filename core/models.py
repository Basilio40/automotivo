from django.db import models
from django import forms

# Create your models here.

class Marca(models.Model):
    # django insere automaticamente um id a  todos os modelos (autoincrementado) 
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Automotivo(models.Model):
    patente = models.CharField(max_length=10, unique=True)
    modelo = models.CharField(max_length=50)
    ano = models.IntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return self.patente
    
class Person(models.Model):
    name = models.CharField(max_length=130)
    email = models.EmailField(blank=True)
    job_title = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True)


