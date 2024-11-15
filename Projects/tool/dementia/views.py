from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Details
from .models import Answers
from .models import DoctorInfo
# Create your views here.
def home(request):
    return render(request,'home.html')

def questions(request):
    
    details = Details(
        patient_name=request.POST['name'],
        patient_age=int(request.POST['age']),
        date=request.POST['date'],
        mobile_num=request.POST['number']
    )
    
    details.save()

    return render(request,'tests.html' , {'patient_details' : details })

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
                answers.ans10,
                answers.ans11,
                answers.ans12,
                answers.ans13,
                answers.ans14,
                answers.ans15,
                answers.ans16,
                answers.ans17,
                answers.ans18,
]
    
    return render(request,'result.html' , {'answers_list': ans_list})

def amst_test(request):
    ans=Answers()
    if request.method == "POST":
        ans.test_name=request.POST.get('test_name')
        ans.age = request.POST.get('age')
        ans.time = request.POST.get('time')
        ans.year = request.POST.get('year')
        ans.location = request.POST.get('location')
        ans.recognize_people = request.POST.get('recognizePeople')
        ans.dob = request.POST.get('dob')
        ans.ww1 = request.POST.get('ww1')
        ans.count_backwards = request.POST.get('countBackwards')
        ans.repeat_address = request.POST.get('repeatAddress')
        
        responses = {
            "test_name":ans.test_name,
            'age': ans.age,
            'time': ans.time,
            'year': ans.year,
            'location': ans.location,
            'recognize_people': ans.recognize_people,
            'dob': ans.dob,
            'ww1': ans.ww1,
            'count_backwards': ans.count_backwards,
            'repeat_address': ans.repeat_address
        }
        return render(request, 'test_result.html',{'responses':responses})

def test_taken(request):
    if request.method == 'POST':
        doctor_name = request.POST.get('doctor_name')
        test = request.POST.get('test')  
        additional_tests = request.POST.get('additional_tests')

        doctorinfo = {
            'doctor_name': doctor_name,
            'test': test,
            'additional_tests': additional_tests
        }

        if test=='mmse': 
            return render(request, 'mmse.html', doctorinfo)
        elif test=="amst":
            return render(request, 'amst.html', doctorinfo) 
