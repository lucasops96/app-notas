from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Nota(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User,on_delete=models.PROTECT,verbose_name='Autor',related_name='notas')

    def __str__(self):
        return self.titulo