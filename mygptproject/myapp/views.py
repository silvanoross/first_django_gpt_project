from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import QuestionForm
from django.urls import reverse
import os
import requests
import openai


def index(request):
    return HttpResponse("Hello, world!")

# Create your views here.

def ask_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            # Do something with the form data
            question_text = form.cleaned_data['question_text']
            # ... (e.g. save to database)
            answer = "we received your question"
            
            return HttpResponseRedirect("/thanks/")
    else:
        form = QuestionForm()
    return render(request, 'ask_question.html', {'form': form})

def thanks(request):
    if request.method == 'POST':
        thank_you = "thank you"
        return render(request, 'thanks.html', {'thank_you':thank_you})
        



    
    