from django.db import models
from django.http import HttpResponse
from .models import Usuario

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    senha = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.nome