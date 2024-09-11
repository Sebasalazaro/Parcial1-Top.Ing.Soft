from django.urls import path

from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("registrar/", views.registrar_vuelo, name="registrar_vuelo"),
    path("lista/", views.lista_vuelo, name="lista_vuelo")
]
