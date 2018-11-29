from django.db import models

#Timezone para obtener la fecha
from django.utils.timezone import now

#Modelo User.
from django.contrib.auth.models import User

# Modelo para la Categoria.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Categoria')

    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateField(auto_now=True, verbose_name='Fecha de Modificación')

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ['-created']

    def __str__(self):
        return self.name

#Modelo para la entrada
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    content = models.TextField(verbose_name='Contenido')
    published = models.DateTimeField(verbose_name='Fecha de Publicación', default=now)
    image = models.ImageField(verbose_name='Imagen', upload_to='blog', blank=True, null=True)

    #Llaves foraneas
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name='Categorias', related_name='get_posts')

    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateField(auto_now=True, verbose_name='Fecha de Modificación')

    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        ordering = ['-created']

    def __str__(self):
        return self.title