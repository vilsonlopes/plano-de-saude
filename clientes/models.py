from django.db import models

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    situation_choices = (
        ('A', 'ADIMPLENTE'),
        ('I', 'INADIMPLENTE'),
    )

    gender = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )

    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14)
    rg = models.CharField(max_length=50)
    telefone = models.CharField(max_length=255)
    sexo = models.CharField(max_length=1, choices=gender, blank=True)
    email = models.CharField(max_length=255, blank=True)
    data_inclusao = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    situacao = models.CharField(max_length=1, choices=situation_choices, default='A')
    observacao = models.TextField(blank=True)
    mostrar = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
