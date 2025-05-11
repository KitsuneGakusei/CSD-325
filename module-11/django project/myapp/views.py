from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Long says Hello!")

# Create your views here.
