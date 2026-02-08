from django.shortcuts import HttpResponse
from django.template import loader

from .models import Question, Choice

def index(request):
    questions_list = Question.objects.all()
    template = loader.get_template('polls/index.html')
    
    res = template.render({'questions_list': questions_list})
    return HttpResponse(res)   

def detail(request, question_id):
    questions = Question.objects.all()
    res = ", ".join([q.question_text for q in questions])
    return HttpResponse(res)    

def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}.")

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")
