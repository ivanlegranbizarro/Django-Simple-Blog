from .managers import PostManager
from django.urls import reverse
from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Category(models.Model):
    name = models.CharField('Nombre', max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['name']


class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name="Título")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Autor")
    body = RichTextField('Entrada', blank=True, null=True)
    created_at = models.DateTimeField(
        'Fecha de publicación', auto_now_add=True)
    updated_at = models.DateTimeField('Fecha de modificación', auto_now=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name='Categoría')
    objects = PostManager()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')
