from django.shortcuts import render, get_object_or_404

# Modelo de Post
from blog.models import Post, Category


# Create your views here.
def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})


def category(request, category_id):
    # category = Category.objects.get(id=category_id)
    # Usar para controlar error y arrojar un 404
    category = get_object_or_404(Category, id=category_id)

    """NO RECOMENDADO"""
    # Me filtra los post de una categoria
    #posts = Post.objects.filter(categories=category)
    """RECOMENDADO ES AGREGAR EL CAMPO related_name='', en el campo del modelo, y usarlo en la vista"""
    return render(request, 'blog/category.html', {'category': category})
