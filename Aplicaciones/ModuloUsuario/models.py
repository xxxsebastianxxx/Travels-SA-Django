from django.db import models

from django.db import models

# Create your models here.

class Usuario(models.Model):
    id = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length= 80)
    apellido = models.CharField(max_length=80)
    telefono = models.CharField(max_length=80)
    correo = models.EmailField(max_length=100)
    
    
 