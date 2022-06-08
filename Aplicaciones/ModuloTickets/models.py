from django.db import models

# Create your models here.

class tickets(models.Model):
     id = models.AutoField(primary_key= True)
     inicio = models.CharField(max_length= 80)
     destino = models.CharField(max_length= 80)
     tarifa = models.BigIntegerField(max_length= 80)
     horario = models.CharField(max_length =80)


class Ciudades(models.Model):
    ciudad = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'ciudades'

class Ciudadesd(models.Model):
    ciudad = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'ciudadesd'