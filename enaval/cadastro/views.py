from django.shortcuts import render, redirect, get_object_or_404
from .forms import FunciForm, LoginForm
from .models import Funcionario
from django.views.generic import ListView


class IndexView(ListView):
    template_name = 'Crud/index.html'
    context_object_name = 'funcionario_list'

    def get_queryset(self):
        return Funcionario.objects.all()


def postview(request):
    if request.method == 'POST':
        form = FunciForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    form = FunciForm()
    return render(request, 'Crud/post.html', {'form': form})


def edit(request, pk, template_name='Crud/edit.html'):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    form = FunciForm(request.POST or None, instance=funcionario)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form': form})


def delete(request, pk, template_name='Crud/confirm_delete.html'):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    if request.method == 'POST':
        funcionario.delete()
        return redirect('index')
    return render(request, template_name, {'object': funcionario})


def loginview(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            senha = form.cleaned_data['senha']
            if nome == 'enaval' and senha == '123456':
                return redirect('index')
    return render(request, 'login.html')
