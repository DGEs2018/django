from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseDirect
from django.urls import path

from .models import Choice, Question

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response ("You're looking at the result of question %s.")

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def index(request):
    latest_question_list = Question.objects_order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice =
        question.choice_set.get(pk)