from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.welcome, name='welcome'),
    url(r'^search/', viws.search_results, name='search_results')
]