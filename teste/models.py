from django.db import models

class Modelo(models.Model):
    nome = models.CharField(max_length=255)