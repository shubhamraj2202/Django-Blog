from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #here we can return HTML CODE
    return HttpResponse("<h2> Hey!!!!! </h2>")



# Create your views here.
