from django.urls import path
from . import views

urlpatterns = [
	path('', views.listar_receitas, name='listar_receitas'),
	path('nova/', views.nova_receita, name='nova_receita'),
	path('editar/<int:id>/', views.editar_receita, name='editar_receita'),
	path('deletar/<int:id>/', views.deletar_receita, name='deletar_receita'),
]