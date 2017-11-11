from django.conf.urls import url

from . import views

app_name = 'index'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'li/$', views.get_name, name='names'),
    url(r'thanks/$', views.haha_name, name='thanks'),
]
