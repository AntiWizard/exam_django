from django.urls import path

from quiz.views import index, show_quiz, show_result

urlpatterns = [
    path('', index, name='index'),
    path('quiz/', show_quiz, name='quiz_list'),
    path('quiz/result', show_result, name='quiz_result')
]
