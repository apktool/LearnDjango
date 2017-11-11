#from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .forms import NameForm

# Create your views here.
def index(request):
    response = HttpResponse('<h1> Hello Wolrd <h1>')
    return response


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # This URL is equal to acation's uri in names.html usually.
            # It's OK if redirect url is different with uri in name.html, But
            # the goal that validate form will lost the purpose.
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'names.html', {'form': form})


def haha_name(request):
    if request.method == 'POST':
        your_name = request.POST.get('your_name')
        your_password = request.POST.get('your_password')

    print('-------.,>')
    return render(request, 'user.html', {'name': your_name, 'password': your_password})
