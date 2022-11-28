from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from quiz.models import Question, Choice


# Create your views here.


@login_required
def show_quiz(request):
    questions = Question.objects.order_by('?')[:5]
    dict_questions = {}
    for question in questions:
        dict_questions[question.id] = list(
            Choice.objects.filter(question_id=question.id).order_by("?").values_list('choice', 'answer'))

    context = {
        "questions": questions,
        "dict_questions": dict_questions
    }
    return render(request, "quiz/quiz_list.html", context=context)


def index(request):
    return render(request, "quiz/index.html", )


def show_result(request):
    if request.POST:
        result = dict(request.POST)
        true = 0
        false = 0
        for key, value in result.items():
            if "True" in result[key]:
                true += 1
            elif "False" in result[key]:
                false += 1
        score = true * 20
        context = {
            "true": true,
            "false": false,
            "score": score
        }
        return render(request, "quiz/quiz_result.html", context=context)
