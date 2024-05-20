from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import *
import random
# Create your views here.




def home(request):
    context={'categories':Category.objects.all()}

    if request.GET.get('category'):
        return redirect(f"/quiz/?category={request.GET.get('category')}")

    return render(request,'home.html',context)

def quiz(request):
    # category = request.GET.get('category')
    # question_obj=Question.objects.filter(category__Category_name__icontains=category)
    # print(question_obj)
    # context={
    #     'category':category,
    #     'question':question_obj,
    #     "answers":question_obj.get_answer(),
    question_obj=(Question.objects.all())

    if request.GET.get('category'):
        question_obj=Question.objects.filter(category__Category_name__icontains=request.GET.get('category'))
    
    question_obj=list(question_obj)
    data={}
    random.shuffle(question_obj)
    for question in question_obj:
        data["category"] = question.category.Category_name
        data["questions"] = question.question
        data['marks'] = question.marks
        data["answers"] = question.get_answer()
    
    print(data)
    return render(request,'quiz.html',data)

def get_quiz(request):  # sourcery skip: for-append-to-extend, list-comprehension, move-assign-in-block
    try:
        question_obj=(Question.objects.all())

        if request.GET.get('category'):
            question_obj=question_obj.filter(category__Category_name__icontains="request.GET.get('category')")
        question_obj=list(question_obj)
        data=[]
        random.shuffle(question_obj)
        for question in question_obj:
            data.append(
                {
                    "category":question.category.Category_name,
                    "question":question.question,
                    "marks":question.marks,
                    "answers":question.get_answer(),
                }
            )

        payload={
            'status':True,'data':data
        }

        print(payload)

        return JsonResponse(payload,safe=False)

    except Exception as e:
        print(e)
        return HttpResponse("Something went wrong")
    