from django.shortcuts import render, redirect, HttpResponse
from .models import Investimentos
from .forms import InvestimentoForm


def novo_investimento(request):
    return render(request, "investimentos/novo_investimento.html")


def investimentos(request):
    dados = {'dados': Investimentos.objects.all()}
    return render(request,"investimentos/investimentos.html", context=dados)
def detalhe(request, id_investimento):
    dados = {
        'dados' : Investimentos.objects.get(pk=id_investimento)
        }
    return render(request, "investimentos/detalhe.html",dados)

def criar(request):
    if request.method == 'POST':
        investimento_form = InvestimentoForm(request.POST)
        if investimento_form.is_valid():
            investimento_form.save()
        return redirect('investimentos')
    else:
        investimento_form = InvestimentoForm()
        formulario = {
            'formulario': investimento_form
        }
        return render(request,'investimentos/novo_investimento.html', context=formulario)

def editar(request, id_investimento):
    investimento = Investimentos.objects.get(pk=id_investimento)
    # novo_investimento/1 -> GET
    if request.method == 'GET':
        formulario = InvestimentoForm(instance=investimento)
        return render(request, 'investimentos/novo_investimento.html',{'formulario': formulario})
    # caso requisição seja POST
    else:
        formulario = InvestimentoForm(request.POST, instance=investimento)
        if formulario.is_valid():
            formulario.save()
        return redirect('investimentos')

def excluir(request, id_investimento):
    investimento = Investimentos.objects.get(pk=id_investimento)
    if request.method == 'POST':
        investimento.delete()
        return redirect('investimentos')
    return render(request, 'investimentos/confimar_exclusao.html',{'item':investimento})

