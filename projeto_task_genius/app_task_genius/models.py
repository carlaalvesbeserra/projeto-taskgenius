from django.db import models

class Tarefa(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, null=False)
    prazo = models.CharField(max_length=100, null=False)
