from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('maquinas/', views.maquinas, name='maquinas'),
    path('quienes_somos/', views.quienes_somos, name='quienes_somos'),
]
