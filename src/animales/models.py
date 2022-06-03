from django.db import models

# Create your models here.
class Animal(models.Model):
    especie = models.TextField()        
    dieta = models.TextField()