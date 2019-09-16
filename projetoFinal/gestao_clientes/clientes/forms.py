from django.forms import ModelForm
from .models import Pessoa


class PersonForm(ModelForm):
    class Meta:  # dizemos ao Django qual modelo deverá ser usado para criar este formulário (model = Pessoa)
        model = Pessoa
        fields = ['first_name', 'last_name', 'age', 'salary', 'photo']
