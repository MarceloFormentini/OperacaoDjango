from django.test import TestCase
from django.urls import reverse
from .models import Receita

class ReceitaTests(TestCase):

	def setUp(self):
		self.receita = Receita.objects.create(
			titulo='Bolo de Chocolate',
			ingredientes='Farinha, ovos, chocolate, leite',
			modo_preparo='Misturar tudo e assar por 40 minutos.'
		)

	def test_listar_receitas(self):
		response = self.client.get(reverse('listar_receitas'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Bolo de Chocolate')

	def test_criar_receita(self):
		data = {
			'titulo': 'Bolo de Laranja',
			'ingredientes': 'Farinha, ovos, suco de laranja',
			'modo_preparo': 'Misturar e assar por 35 minutos.'
		}
		response = self.client.post(reverse('nova_receita'), data)
		self.assertEqual(response.status_code, 302)
		self.assertEqual(Receita.objects.count(), 2)

	def test_editar_receita(self):
		response = self.client.post(reverse('editar_receita', args=[self.receita.id]), {
			'titulo': 'Bolo de Chocolate com Morango',
			'ingredientes': self.receita.ingredientes,
			'modo_preparo': self.receita.modo_preparo
		})
		self.assertEqual(response.status_code, 302)
		self.receita.refresh_from_db()
		self.assertEqual(self.receita.titulo, 'Bolo de Chocolate com Morango')

	def test_excluir_receita(self):
		response = self.client.post(reverse('deletar_receita', args=[self.receita.id]))
		self.assertEqual(response.status_code, 302)
		self.assertEqual(Receita.objects.count(), 0)
