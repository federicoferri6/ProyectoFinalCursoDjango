from django.shortcuts import render_to_response, RequestContext
from apps.stock.forms import ProductForm
from apps.stock.models import Product, PACKAGE_TYPE
from django.contrib.auth.decorators import login_required


"""Vistas que requieren estar autenticado
"""


"""Muestra un formulario para ingresar un nuevo producto
"""


@login_required
def new_product(request):
    form = ProductForm()
    if request.method == 'POST':
        # Si es un POST se guardan los datos en la base de datos
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
    # Se muestra el formulario
    return render_to_response(
        'stock/new_product.html',
        RequestContext(
            request,
            {
                'form': form
            }
        ),
    )


""" Obtiene todos los productos de la base de datos y renderiza un html con
una tabla con los productos.
"""


@login_required
def product_list(request):
    product_list = Product.objects.all()
    return render_to_response(
        'stock/product_list.html',
        RequestContext(
            request,
            {
                'list': product_list,
                'package': PACKAGE_TYPE,

            }
        ),
    )
