from django.shortcuts import render, get_object_or_404, redirect
from .models import Tarefa

def index(request):
    return render(request, 'index.html')

def tarefas(request):
    if request.method == 'POST':
        # Salvando os dados da tela para o banco
        nova_tarefa = Tarefa()
        nova_tarefa.titulo = request.POST.get('titulo')
        nova_tarefa.prazo = request.POST.get('prazo')
        nova_tarefa.save()
        # Redirecionar para a página de listagem
        return redirect('lista')
    # Exibindo as tarefas cadastradas
    tarefas = {
        'tarefas': Tarefa.objects.all()
    }
    # Retornar os dados para a página de listagem
    return render(request, 'lista.html', tarefas)

def lista(request):
    tarefas = {
        'tarefas': Tarefa.objects.all()
    }
    return render(request, 'lista.html', tarefas)

def editar(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    if request.method == 'POST':
        # Recuperar a tarefa existente e atualizar seus atributos com os dados do formulário
        tarefa.titulo = request.POST.get('titulo')
        tarefa.prazo = request.POST.get('prazo')
        tarefa.save()
        return redirect('lista')
    return render(request, 'editar.html', {'tarefa': tarefa})

def excluir(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('lista')
    return render(request, 'excluir.html', {'tarefa': tarefa})
