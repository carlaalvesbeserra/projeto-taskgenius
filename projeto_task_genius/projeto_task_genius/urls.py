from django.urls import path
from django.contrib import admin 
from app_task_genius import views

urlpatterns = [
    # rota, view responsável, nome de referência
    path('admin/', admin.site.urls, name='admin'),
    path('', views.index, name='index'),
    path('tarefas/', views.tarefas, name='tarefas'),
    path('lista/', views.lista, name='lista'),
    path('editar/<id>/', views.editar, name='editar'),
    path('excluir/<id>/', views.excluir, name='excluir'),
]
