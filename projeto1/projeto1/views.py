from django.http import HttpResponse
from django.shortcuts import render


def anne(request):
    return render(request, 'index.html')


def ano(request, year):
    return HttpResponse("O ano passado foi:" + str(year))


def funcnome(nome):
    lista_nomes = [
        {'nome': 'Caroline', 'idade': 22},
        {'nome': 'Yuna', 'idade': 5},
    ]
    for pessoa in lista_nomes:
        if pessoa['nome'] == nome:
            return pessoa
    else:
        return {'idade': 0}


def fnome(request, nome):
    result = funcnome(nome)
    print(result)
    if result['idade'] > 0:
        return HttpResponse('O nome é ' + result['nome'])
    else:
        return HttpResponse('Pessoa não encontrada')


def fnome2(request, nome):
    name = funcnome(nome)
    return render(request, 'nome.html', {'v_name': name})  # está retornando a váriavel name p template nome.html
