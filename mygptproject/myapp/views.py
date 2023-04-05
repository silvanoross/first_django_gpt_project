from django.shortcuts import render
from django.http import HttpResponse
from .forms import QuestionForm

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
    else:
        form = QuestionForm()
    return render(request, 'ask_question.html', {'form': form})
