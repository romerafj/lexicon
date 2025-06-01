from django.urls import path
from . import views # Asegúrate de que esta línea esté presente

urlpatterns = [
    path('', views.index, name='index'), # <--- ¡Añade esta línea!
]