from django.shortcuts import render, redirect, \
    get_object_or_404  # redirect consegue mandar uma pessoa p uma url, no caso a person_list
# get object é para pegar o objeto do usuário e caso não consiga, retorna um 404
from .models import Pessoa
from .forms import PersonForm


def person_list(request):
    persons = Pessoa.objects.all()  # é como um select * from Pessoa, ou seja, busca todas as pessoas
    return render(request, 'person.html', {"galeres": persons})


def person_new(request):
    form = PersonForm(request.POST or None,
                      request.FILES or None)  # o files são para pegar os arquivos de midia mandados

    if form.is_valid():
        form.save()
        return redirect('person_list')  # após concluir a ação, irá redirecionar para a lista
    return render(request, 'person_form.html', {'form': form})


def person_update(request, id):
    pessoa = get_object_or_404(Pessoa, pk=id)  # o pk é que vai procurar a pessoa atraves do id no banco de dados, o pk é o id no bd / Pessoa é no models
    form = PersonForm(request.POST or None, request.FILES or None, instance=pessoa) # PersonForm é no forms.py
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})

def person_delete(request, id):
    pessoa = get_object_or_404(Pessoa, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=pessoa) # não sei como isso se dá, mas o form nesse caso é usado
    #para quando clicarmos em deletar, ir para o formulário da pessoa. Caso não seja necessário, podemos apenas deixar a página com o botão delete

    if request.method == 'POST': # se o usuario usar http post, retornará TRUE, se não, retornará FALSE
        pessoa.delete()
        return redirect('person_list')
    return render(request, 'person_delete_confirm.html', {'form': form})

