from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("button reporter index.")
# Create your views here.
