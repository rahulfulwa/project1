from polls.models import Question, Choice
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse


# def hello_world(request):
#     print("this is my first view Hello World!")
#     return HttpResponse('<h1>Hello World! how are you</h1>')
#

# Create your views here.
def main_page(request):
    all_questions_list = Question.objects.all()
    print(all_questions_list)
    context = {
        'question_list': all_questions_list
    }
    return render(request, "polls/main_page.html", context)


def details(request, ques_id):
    qs = Question.objects.filter(pk=ques_id)
    # if the question exist in the Question Table
    # than we will access its text
    if qs:
        qs_text = qs[0]
        # now fetch the choices for it
        choice_list = Choice.objects.filter(question=qs_text)
        # now make a dict to show it in the web page
        context = {
            'question': qs_text,
            'choice_list': choice_list,
        }
        print(qs, choice_list)
        return render(request, 'polls/details.html', context)
    # else:
    #     response = "Question with id=" + str(id) + " not found."
    #     return HttpResponse(response)


def results(request, ques_id):
    question_qs = Question.objects.filter(pk=ques_id)
    if question_qs:
        question = question_qs[0]
        choice_list = Choice.objects.filter(question=question)
        context = {
            'question': question,
            'choice_list': choice_list,
        }
        return render(request, 'polls/results.html', context)
    else:
        response = "there is no such question"
        return HttpResponse(response)


def vote(request, ques_id):
    # whatever value we have submitted through form is in dictionary
    selected_choice_id = request.POST['choice']
    selected_choice_qs = Choice.objects.filter(pk=selected_choice_id)
    if selected_choice_qs:
        selected_choice = selected_choice_qs[0]
        selected_choice.No_of_votes += 1
        selected_choice.save()
        print(reverse('Results', kwargs={'ques_id': ques_id}))
        return HttpResponseRedirect(reverse('Results', kwargs={'ques_id': ques_id}))
    else:
        response = "Choice with this id is not present."
        return HttpResponse(response)
