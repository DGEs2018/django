from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello user, welcome to the polls index.')

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response ("You're looking at the result of question %s.")

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)