from django.db import models


# Create your models here.
class Link(models.Model):
    key = models.CharField(max_length=100, verbose_name="Nombre Clave", unique=True)
    name = models.CharField(max_length=200, verbose_name="Red Social")
    url = models.URLField(max_length=200, verbose_name="Enlace", blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "enlace"
        verbose_name_plural = "enlaces"
        ordering = ['name']

    def __str__(self):
        return self.name
