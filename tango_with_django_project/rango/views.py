from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def about(request):
    return HttpResponse("Rango says here is the about page! <a href='/rango/'>Index</a> ")

def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)
