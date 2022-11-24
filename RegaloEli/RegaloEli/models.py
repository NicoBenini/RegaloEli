from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

##########################################################
# MODELS DEL regalo
##########################################################
class Modelo(models.Model):
    class Meta:
        verbose_name_plural = "Modelos"

    modelo = models.CharField(max_length=40)
    
    def __str__(self):
        return self.modelo
    
class Memoria(models.Model):
    class Meta:
        verbose_name_plural = "Memorias"

    memoria = models.CharField(max_length=40)
    
    def __str__(self):
        return self.memoria

class Color(models.Model):
    class Meta:
        verbose_name_plural = "Colores"
    
    color = models.CharField(max_length=40)

    def __str__(self):
        return self.color