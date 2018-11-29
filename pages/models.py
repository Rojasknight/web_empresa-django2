from django.db import models

#Ckeditor para contenido
from ckeditor.fields import RichTextField


# Create your models here.
class Page(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Titulo")
    contenido = RichTextField(verbose_name="Contenido")
    # Campo para ordenar en el template
    order = models.SmallIntegerField(verbose_name='Orden', default=0)

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "pagina"
        verbose_name_plural = "paginas"
        ordering = ['order', 'titulo']

    def __str__(self):
        return self.titulo
