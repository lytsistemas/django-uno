from django.urls import path
from . import views

# Definir el espacio de nombres para esta aplicación
app_name = "polls"

# Definir las rutas URL para la aplicación de encuestas
urlpatterns = [
    # Ruta para la vista de índice
    path("", views.IndexView.as_view(), name="index"),
    # Ruta para la vista de detalles de una pregunta específica
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # Ruta para la vista de resultados de una pregunta específica
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # Ruta para la acción de votar en una pregunta específica
    path("<int:question_id>/vote/", views.vote, name="vote"),
]