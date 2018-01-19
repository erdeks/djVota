from django.db import models

class Pregunta(models.Model):
    texto = models.CharField(max_length=200)
    fecha_publicacion = models.DateTimeField('Fecha Publicacion')
    def __str__(self):
        return self.texto
    

class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)
    def __str__(self):
        return self.texto
