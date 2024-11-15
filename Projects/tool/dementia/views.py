from django.shortcuts import render

from .models import Details
from .models import Answers
# Create your views here.
def home(request):
    return render(request,'home.html')

def questions(request):
    
    details = Details()
    details.patient_name=request.POST['name']
    details.patient_age=int(request.POST['age'])
    details.date=request.POST['date']
    details.mobile_num=request.POST['number']


    return render(request,'questions.html' , {'patient_details' : details })

def checking(request):

    answers = Answers()
    answers.ans1 =request.POST['q1']
    answers.ans2 =request.POST['q2']
    answers.ans3 =request.POST['q3']
    answers.ans4 =request.POST['q4']
    answers.ans5 =request.POST['q5']
    answers.ans6 =request.POST['q6']
    answers.ans7 =request.POST['q7']
    answers.ans8 =request.POST['q8']
    answers.ans9 =request.POST['q9']
    answers.ans10 =request.POST['q10']
    answers.ans11 =request.POST['q11']
    answers.ans12 =request.POST['q12']
    answers.ans13 =request.POST['q13']
    answers.ans14 =request.POST['q14']
    answers.ans15 =request.POST['q15']
    answers.ans16 =request.POST['q16']
    answers.ans17 =request.POST['q17']
    answers.ans18 =request.POST['q18']

    ans_list = [answers.ans1,
                answers.ans2,
                answers.ans3,
                answers.ans4,
                answers.ans5,
                answers.ans6,
                answers.ans7,
                answers.ans8,
                answers.ans9,
                answers.ans10 ,
                answers.ans11 ,
                answers.ans12 ,
                answers.ans13 ,
                answers.ans14 ,
                answers.ans15 ,
                answers.ans16 ,
                answers.ans17 ,
                answers.ans18 ,
]
    
    return render(request,'result.html' , {'answers_list': ans_list})