from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('maquinas/', views.maquinas, name='maquinas'),
]
