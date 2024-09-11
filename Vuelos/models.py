from django.db import models

class Vuelo(models.Model):
    idVuelo = models.AutoField(primary_key=True)
    nombreVuelo = models.CharField(max_length=50)
    tipoVuelo = models.CharField(max_length=15)
    precioVuelo = models.CharField(max_length=15)

    
