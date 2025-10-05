from django.urls import path
from django.http import HttpResponse
from . import views

def index(request):
    return HttpResponse("Hello")