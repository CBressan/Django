from django.db import models

#sempre que fizer alterações, fazer o makemigrations

class Pessoa(models.Model):
    first_name = models.CharField(max_length=30)  # o first name vai ter no maximo 30 caracteres
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)  # duas casas depois da vírgula
    bio = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='clients.photos', null=True, blank=True) #caso queira salvar as fotos em uma
    #pasta dentro da pasta de media, a partir do null, é só caso seja opcional

    def __str__(self):
        return self.first_name + ' ' + self.last_name
