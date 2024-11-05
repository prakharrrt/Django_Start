from django.shortcuts import render, HttpResponse
from .models import Question
from django.template import loader
from django.http import Http404
# Create your views here.
def index(request):
    # return render(request,'index.html')
    
    
    # ques_list=Question.objects.order_by('-pub_date')[:5]
    # output=', '.join([q.question_text for q in ques_list])
    # return HttpResponse(output)

    # latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # template = loader.get_template("C:/Users/Prakhar/Django_Project/Home/templates/index.html")
    # context = {
    #     "latest_question_list": latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))

    # shortcut for the above method
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    context={"latest_question_list":latest_question_list}
    return render(request,'index.html',context)



def about(request):
    return HttpResponse('this is the about page')

def service(request):
    return HttpResponse('this is the service page')

def contact(request):
    return HttpResponse('this is the contact page')



# detail(request=<HttpRequest object>, question_id=34)
def detail(request, question_id):
    # return HttpResponse(f"You are looking at question {question_id}")

    try:
        question=Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request,'details.html',{"question":question})

def results(request, question_id):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)