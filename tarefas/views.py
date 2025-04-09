from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Receita

def listar_receitas(request):
	receitas = Receita.objects.all()
	return render(request, 'listar.html', {'receitas': receitas})

def nova_receita(request):
	if request.method == 'POST':
		Receita.objects.create(
			titulo=request.POST['titulo'],
			ingredientes=request.POST['ingredientes'],
			modo_preparo=request.POST['modo_preparo']
		)
		return redirect('listar_receitas')
	return render(request, 'nova.html')

def editar_receita(request, id):
	receita = get_object_or_404(Receita, pk=id)
	if request.method == 'POST':
		receita.titulo = request.POST['titulo']
		receita.ingredientes = request.POST['ingredientes']
		receita.modo_preparo = request.POST['modo_preparo']
		receita.save()
		return redirect('listar_receitas')
	return render(request, 'editar.html', {'receita': receita})

def deletar_receita(request, id):
	receita = get_object_or_404(Receita, pk=id)
	receita.delete()
	return redirect('listar_receitas')