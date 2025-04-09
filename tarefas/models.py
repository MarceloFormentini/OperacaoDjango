from django.db import models

class Receita(models.Model):
	titulo = models.CharField(max_length=200)
	ingredientes = models.TextField()
	modo_preparo = models.TextField()

	def __str__(self):
		return self.titulo