from django.shortcuts import render

# Create your views here.

def lista_tarefas(request):
    tarefas = ['Sistemas de Informação', 'Curso de Django', 'Curso de Python']
    return render(request, 'lista_tarefas.html', {'tarefas': tarefas})
