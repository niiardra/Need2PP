from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("button reporter index.")

def floor(request, floor_id):
    return HttpResponse("You are looking at the page for floor %s" % floor_id)

def washroom(request, washroom_id):
    return HttpResponse("This is the page for washroom %s. The Gender is: " % washroom_id)
