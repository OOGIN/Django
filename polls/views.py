from django.shortcuts import render
from django.http import HttpResponse

def index(requset):
    return HttpResponse("급여일 까지 4일 남았당")

# Create your views here.
