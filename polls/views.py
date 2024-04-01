from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.template import loader
from django.http import Http404
from django.urls import reverse


# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     template = loader.get_template("polls/index.html")
#     context = {
#         "latest_question_list": latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:8]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, "polls/detail.html", {"question": question})
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # choice_count = len(question.choice_set.all())
    # content_1 = question.choice_set.all()[0]
    question_list = Question.objects.all()
    context = {
        "question": question,
        "question_list": question_list
    }
    # context = {
    # "question": question,
    # "ch_num": choice_count,
    # "content_1" : content_1
    # }
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

from django.db.models import F
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))