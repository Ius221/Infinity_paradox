from django.shortcuts import render
from django.http import HttpResponse
from . import models	#connect to database through model

# Create your views here.
def fun1(request):
    return render(request,'index.html')