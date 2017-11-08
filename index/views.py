#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return HttpResponse('<h1> Hello Wolrd <h1>')
