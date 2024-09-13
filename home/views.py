from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("This is the django application create, read, update, and, delete for the crud operations also add auth function lib from django")
                        