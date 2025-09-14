from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from polls.models import Choice, Question

# Create your views here.
def index(request):
    latest_question = Question.objects.all().order_by('-pub_date')
    context = {'latest_question' : latest_question }
    return render(request, 'index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question' : question})


def vote(request, question_id ):
    question = get_object_or_404(Question, pk=question_id)
    print("vote start")
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except Exception as e:
        print(e)
        return render(request, 'detail.html', {
            'question' : question, 
            'error_message' : "You didn't select a choice"
        })
    
    selected_choice.votes += 1
    print(f"{selected_choice.votes}")
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'results.html', {'question' : question})