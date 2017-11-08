from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponsePermanentRedirect

class SimpleMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        print("Hello world")


    def __call__(self, request):
        print('Hello world -- >')
        response = self.get_response(request)
        response.set_cookie('user', 'haha')
        return response


    def process_view(self, request, view_func, view_args, view_kwargs):
        user = request.COOKIES.get('user')
        if user is not None:
            print(request.get_host())
            response = HttpResponseRedirect('https://so.com')
            return response
