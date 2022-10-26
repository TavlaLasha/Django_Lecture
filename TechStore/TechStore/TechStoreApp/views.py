from django.shortcuts import render
from django.http import HttpResponse
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

    return render(request, 'TechStoreApp/index.html', context)

def hello(request):
    return HttpResponse("Hello World!")
