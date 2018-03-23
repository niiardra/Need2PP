from django.shortcuts import render
from django.http import HttpResponse
from .models import Floor, Washroom

def index(request):
##    return HttpResponse("button reporter index.")
    return render(request, 'buttonReporter/index.html')

def floor(request, floor_id):
    return render(request, 'buttonReporter/floor.html')

def washroom(request, washroom_id):
    return HttpResponse("This is the page for washroom %s. The Gender is: " % washroom_id)
