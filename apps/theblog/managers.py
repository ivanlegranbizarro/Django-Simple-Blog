from django.db import models


class PostManager(models.Manager):
    def lista_post(self, kword):
        resultado = self.filter(title__icontains=kword)
        return resultado
