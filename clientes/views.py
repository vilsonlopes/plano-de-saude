from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Cliente
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages

# Create your views here.


def index(request):
    clientes = Cliente.objects.all().filter(mostrar=True)

    paginator = Paginator(clientes, 10) # Mostra 10

    page = request.GET.get('page')
    clientes = paginator.get_page(page)

    return render(request, 'clientes/index.html', {
        'clientes': clientes
    })


def detalhes(request, cliente_id):
    #cliente = Cliente.objects.get(id=cliente_id)
    cliente = get_object_or_404(Cliente, id=cliente_id)


    if not cliente.mostrar:
        raise Http404()

    return render(request, 'clientes/detalhes.html', {
        'cliente': cliente
    })


def busca(request):
    termo = request.GET.get('termo')

    if termo is None or not termo:
        messages.add_message(
            request, messages.ERROR, 'Campo de busca não pode ficar vazio.'
        )

        return redirect('index')

    campos = Concat('nome', Value(' '), 'sobrenome')

    clientes = Cliente.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(cpf__icontains=termo)
    )

    paginator = Paginator(clientes, 10)  # Mostra 10

    page = request.GET.get('page')
    clientes = paginator.get_page(page)

    return render(request, 'clientes/busca.html', {
        'clientes': clientes
    })
