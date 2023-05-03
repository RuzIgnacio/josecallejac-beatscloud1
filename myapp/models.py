from django.db import models

# Create your models here.

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=50)
    nombre_artistico = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    repeat_password = models.CharField(max_length=50)
    def str(self):
        return self.nombre_artistico
    
class Tipo_Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    esproductor = models.BooleanField(("True"))
    tipo_user = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    def str(self):
        return self.esproductor