from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Question
from .forms import AnswerForm
from django.utils import timezone


# Create your views here.


def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'q' : question_list}
    return render(request, 'board/question_list.html', context)

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'board/question_detail.html', {'question' : question} )

def answer_create(request, question_id):
    question = Question.objects.get(id=question_id)

    form = AnswerForm(request.POST)
    if form.is_valid():
        answer = form.save(commit=False)
        answer.create_date = timezone.now()
        answer.question = question
        answer.save()
        return redirect('board:detail', question_id=question.id)
        