from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def about(request):
    context_dict1 = {'boldmessage': "Dominik"}
    return render(request, 'rango/about.html', context=context_dict1)

def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)
