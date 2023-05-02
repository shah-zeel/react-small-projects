from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    # Instead of returning plain Http response, we'll return a html markup
    return render(request, 'hello.html', {'name' : 'Mosh'})
