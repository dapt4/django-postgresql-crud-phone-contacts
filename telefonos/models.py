from django.db import models

# Create your models here.
class Dato(models.Model):
    dato_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

