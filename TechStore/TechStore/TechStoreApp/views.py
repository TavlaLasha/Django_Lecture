from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .forms import TestForm


def index(request):
    form = TestForm(request.POST or None)
    context = {
            'form': form
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        context = {
            'form': form,
            'username': username,
            'password': password
        }

    return render(request, 'Home/index.html', context)


@csrf_exempt
def hello(request):
    return HttpResponse("Hello World!")
