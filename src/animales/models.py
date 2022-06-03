from django.db import models

# Create your models here.
class Persona(models.Model):
    especie = models.TextField()        
    dieta = models.TextField()
    