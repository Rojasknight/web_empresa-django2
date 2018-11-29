from django.contrib import admin
from .models import Post, Category


# Admin to category
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    # Mostrar el las columnas de un registro
    list_display = ('title', 'author', 'published', 'post_categories')
    # Ordenar los registros
    ordering = ('author', 'published')
    #Agregar input de busqueda. (author__username)->busca por el nombre del autor
    search_fields = ('title', 'content', 'author__username', 'categories__name')
    #flitro de busqueda por fechas
    date_hierarchy = 'published'
    #filtrar por campos (Son los campos de las relaciones)
    list_filter = ('author__username', 'categories__name')

    #Para listar las categorias de una entrada(obj -> hacer referencia a aun registro, un objeto)
    def post_categories(self, obj):
        return ', '.join([c.name for c in obj.categories.all().order_by('name')])

    #Cambiarle el label "post_categories" por "Categorias"
    post_categories.short_description = 'Categorias'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
