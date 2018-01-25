from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Pregunta(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    texto = models.CharField(max_length=200)
    fecha_publicacion = models.DateTimeField('Fecha Publicacion')
    fecha_expiracion = models.DateTimeField('Fecha Expiracion')
    def __str__(self):
        return self.texto


class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)
    def __str__(self):
        return self.texto
    def votosTotales(self):
        return Voto.objects.filter(respuesta=self).count()

class Voto(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    respuesta = models.ForeignKey(Respuesta , on_delete=models.CASCADE)
