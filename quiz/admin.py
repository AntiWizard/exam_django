from django.contrib import admin

from quiz.models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'content',)


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'choice', 'question', 'answer',)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
