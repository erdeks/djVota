from django.contrib import admin

from .models import Preguntas, Respuestas


class ChoiceInline(admin.TabularInline):
    model = Respuestas
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('texto', 'fecha_publicacion', 'was_published_recently')
    list_filter = ['fecha_publicacion']
    search_fields = ['texto']

admin.site.register(Preguntas, QuestionAdmin)

admin.site.register(Respuestas)
