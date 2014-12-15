from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render_to_response(
        'core/home.html',
        RequestContext(
            request,
            {
                'Titulo': 'Candy Store',
            }
        )
    )
