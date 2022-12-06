from django.shortcuts import render
from django.http import HttpResponse

def index(requset):
    return HttpResponse("여따가 데이터베이스 받은 값을 어떻게 넣어!")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

from .models import Question


# Create your views here.
