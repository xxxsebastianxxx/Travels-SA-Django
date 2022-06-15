from django.db import models

# Create your models here.

class tickets(models.Model):
     id = models.AutoField(primary_key= True)
     nombre = models.CharField(max_length=22)
     inicio = models.CharField(max_length= 80)
     destino = models.CharField(max_length= 80)
     tarifa = models.BigIntegerField(max_length= 80)
     horario = models.CharField(max_length =80)
     bus = models.CharField(max_length=44)

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

class Tarifas(models.Model):
    precios = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tarifas'


class Horario(models.Model):
    hora_salida = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'horario'


class ModulousuarioUsuario(models.Model):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    telefono = models.CharField(max_length=80)
    correo = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'modulousuario_usuario'

class Vehiculos(models.Model):
    marca = models.CharField(max_length=20)
    placa = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'vehiculos'