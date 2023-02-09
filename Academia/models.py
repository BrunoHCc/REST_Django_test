from django.db import models

# Create your models here.

class Aluno(models.Model):
    name= models.CharField(max_length=100, default="Nome")
    peso= models.FloatField()
    idade= models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Professor(models.Model):
    name= models.CharField(max_length=100, default="Nome")
    profissao = models.CharField(max_length=100, default="Nada")

    def __str__(self):
        return self.name

class Aulas(models.Model):
    name= models.CharField(max_length=100)
    prof= models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name