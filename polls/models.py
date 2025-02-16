import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin

# Modelo para las preguntas
class Question(models.Model):
    # Texto de la pregunta
    question_text = models.CharField(max_length=200)
    # Fecha de publicación
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        # Representación en cadena del objeto
        return self.question_text
    
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        # Verifica si la pregunta fue publicada recientemente
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

# Modelo para las opciones de respuesta
class Choice(models.Model):
    # Relación con la pregunta
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # Texto de la opción
    choice_text = models.CharField(max_length=200)
    # Número de votos
    votes = models.IntegerField(default=0)

    def __str__(self):
        # Representación en cadena del objeto
        return self.choice_text