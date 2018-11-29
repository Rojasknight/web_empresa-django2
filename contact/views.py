from django.shortcuts import render, redirect

# Para cargar la url de contact que hay actualmente en url.py
from django.urls import reverse

# Importar el formulario.
from contact.forms import ContactForm


# Create your views here.
def contact(request):
    # instanciamos el el modelo del formulario.
    contact_form = ContactForm()

    # Validar que metodo hay, para posteriormente obtener los datos.
    if request.method == 'POST':
        # rellenamos en el modelo los datos que vienen del formulario.
        contact_form = ContactForm(data=request.POST)
        # validamos que los datos sean validos
        if contact_form.is_valid:
            # el segundo parametro de get(), es por si viene vacio, por defecto me lo deje vacio
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')

            # si todo esta ok, redireccionamos al usuario.
            return redirect(reverse('contact') + '?ok')

    return render(request, 'contact/contact.html', {'form': contact_form})
