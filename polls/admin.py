from django.contrib import admin
# Importamos los modelos Choice y Question
from .models import Choice, Question

# Definimos una clase para mostrar las opciones en línea en el administrador
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3  # Número de opciones adicionales que se mostrarán

# Definimos una clase para personalizar la interfaz del administrador para el modelo Question
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),  # Campo para el texto de la pregunta
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),  # Campo para la fecha de publicación, colapsable
    ]
    inlines = [ChoiceInline]  # Mostrar las opciones en línea
    list_display = ["question_text", "pub_date", "was_published_recently"]  # Campos que se mostrarán en la lista de preguntas
    list_filter = ["pub_date"]  # Filtros disponibles en la lista de preguntas
    search_fields = ["question_text"]  # Campos por los que se puede buscar

# Registramos los modelos en el sitio de administración
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)