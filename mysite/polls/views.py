from django.shortcuts import render
from django.http import HttpResponse



# def index(request):
#     #return HttpResponse("Hello, world. You're at the polls index.")
#     return HttpResponse("Hello, world. 68addc82 is the polls index.")

# Methode 1
from .models import Question
# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     output = ", ".join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)

# Méthode 2
# from django.template import loader
# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     template = loader.get_template("polls/index.html")
#     context = {
#         "latest_question_list": latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

# Méthode 3 - A shortcut: render()¶
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)



# Raising a 404 error
# https://docs.djangoproject.com/en/4.2/intro/tutorial03/ 

# from django.http import Http404

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, "polls/detail.html", {"question": question})


# A shortcut: get_object_or_404()¶
"""
 It’s a very common idiom to use get() and raise Http404 if the object doesn’t exist. Django provides a shortcut. Here’s the detail() view, rewritten:
"""

from django.shortcuts import get_object_or_404, render

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})



def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)