from django.db import models

# Create your models here.
class Invernadero(models.Model):
       Temperatura = models.CharField(max_length=100)
       Humedad = models.TextField(max_length=100)
       Luz = models.TextField()

       def __str__(self):
           return f"{self.Temperatura} - {self.Humedad} - {self.Luz}"
       