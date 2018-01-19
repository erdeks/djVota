import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Preguntas(models.Model):
    texto = models.CharField(max_length=200)
    fecha_publicacion = models.DateTimeField('fecha publicada')
    def __str__(self):
       return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.fecha_publicacion <= now
    was_published_recently.admin_order_field = 'fecha_publicacion'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Publicada Recientemente?'

class Respuestas(models.Model):
    pregunta = models.ForeignKey(Preguntas, on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)
    def __str__(self):
        return self.texto
