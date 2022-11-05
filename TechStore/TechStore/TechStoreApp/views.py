from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from . import models
from .forms import TestForm


def index(request):
    form = TestForm(request.POST or None)
    context = {
            'form': form
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        age = form.cleaned_data.get('age')

        test = models.TestModel(name=username, age=age)
        test.save()

        context = {
            'form': form,
            'username': username,
            'age': age
        }

    return render(request, 'Home/index.html', context)


@csrf_exempt
def hello(request):
    return HttpResponse("Hello World!")
