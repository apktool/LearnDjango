#from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    response = HttpResponse('<h1> Hello Wolrd <h1>')
    response.set_cookie('user', 'haha')
    return response


def terms(request):
    return HttpResponseRedirect('/polls')
