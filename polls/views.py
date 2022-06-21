from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . models import Question
from django.http import Http404
from django.shortcuts import get_object_or_404
# Create your views here.
#def index(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)
   
#def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")

#def index(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    #context = {
        #'latest_question_list' : latest_question_list,
    #}
    #return HttpResponse(template.render(context, request))

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = { 'lattest_question_list' : latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    #question = get_object_or_404(Question, pk=question_id) #alternative to try excpet block
    return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id) #messed


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)





