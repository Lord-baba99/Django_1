from django.shortcuts import render
from .models import Question
from django.http import Http404
from django.http import HttpResponse

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    """ output = ', '.join([q.question_text for q in latest_question_list])
    template = loader.get_template('polls/index.html')"""
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    try: 
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist :
        raise Http404("La question n'existe pas.")
    return render(request, 'polls/detail.html', {'question' : question})


def results(request, question_id):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")

