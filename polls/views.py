from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question

# Vista genérica para la página de índice que muestra las últimas cinco preguntas publicadas
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Devuelve las últimas cinco preguntas publicadas (sin incluir las que se publicarán en el futuro).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]

# Vista genérica para mostrar los detalles de una pregunta específica
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        Excluye cualquier pregunta que no esté publicada aún.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

# Vista genérica para mostrar los resultados de una pregunta específica
class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

# Función para manejar el voto de una pregunta específica
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Volver a mostrar el formulario de votación de la pregunta si no se seleccionó una opción válida
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "No seleccionaste una opción.",
            },
        )
    else:
        # Incrementar el número de votos de la opción seleccionada
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Redirigir a la página de resultados después de manejar correctamente los datos POST
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))