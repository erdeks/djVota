from django.contrib import admin

from .models import Respuesta, Pregunta
class RespuestaEnLinea(admin.TabularInline):
    model = Respuesta
    extra = 3
class PreguntaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informacion de Encuesta',               {'fields': ['texto']}),
        ('Informacion de Fecha', {'fields': ['fecha_publicacion']}),
    ]
    inlines = [RespuestaEnLinea]
    list_display = ('texto', 'fecha_publicacion')
    list_filter = ['fecha_publicacion']
    search_fields = ['texto']
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Respuesta)
