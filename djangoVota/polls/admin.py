from django.contrib import admin

from .models import Respuesta, Pregunta, Voto
class RespuestaEnLinea(admin.TabularInline):
    model = Respuesta

class RespuestaAdmin(admin.ModelAdmin):
    list_display = ('texto', 'pregunta', 'votosTotales')
    search_fields = ['texto']
    ordering = ['-pregunta']
class PreguntaAdmin(admin.ModelAdmin):
    inlines = [RespuestaEnLinea]
    list_display = ('texto', 'fecha_publicacion')
    list_filter = ['fecha_publicacion']
    search_fields = ['texto']
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(autor=request.user)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Respuesta, RespuestaAdmin)
admin.site.register(Voto)
