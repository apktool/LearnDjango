from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin

class SimpleMiddleware(MiddlewareMixin):

    def __init__(self, request=None):
        print("Hello world")

    def process_request(self, request=None):
        reponse = HttpResponseRedirect('https://so.com')
        return reponse
