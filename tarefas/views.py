from django.shortcuts import render, redirect
from .models import Tarefa
# Create your views here.

def lista_tarefas(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        if titulo:
            Tarefa.objects.create(titulo=titulo)
            return redirect('lista_tarefas')

    tarefas = Tarefa.objects.all()
    return render(request, 'lista_tarefas.html', {'tarefas': tarefas})
