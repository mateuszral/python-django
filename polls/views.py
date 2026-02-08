from django.shortcuts import HttpResponse, render, get_object_or_404

from .models import Question, Choice

def index(request):
    questions_list = Question.objects.all()
    
    res = render(request, 'polls/index.html', {'questions_list': questions_list})
    return res   

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    choices = Choice.objects.filter(question_id = question_id)
    return render(request, 'polls/results.html', {'choices': choices})

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")
