from django.shortcuts import render
from django.urls import reverse
from .models import Details
from .models import Answers
from .models import AmstAnswers
from .models import DoctorInfo
from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404

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
        ans = AmstAnswers(
            test_name=request.POST.get('test_name'),
            age=int(request.POST.get('age')),
            time=request.POST.get('time'),
            year=int(request.POST.get('year')),
            location=request.POST.get('location'),
            recognize_people=request.POST.get('recognizePeople'),
            dob=request.POST.get('dob'),
            ww1=int(request.POST.get('ww1')),
            count_backwards=request.POST.get('countBackwards'),
            repeat_address=request.POST.get('repeatAddress')
        )
        
        ans.save()
        
        patient_name = request.POST.get('patient_name')
        try:
            patient_details = Details.objects.get(patient_name=patient_name)
            match_message = (
                "The age matches with the entered details."
                if ans.age == patient_details.patient_age
                else "The age does not match the entered details."
            )
        except Details.DoesNotExist:
            match_message = "No patient details found."

        return render(request, 'test_result.html', {'responses': ans, 'match_message': match_message})

def test_taken(request):
    doctor_details = DoctorInfo(
        doctor_name=request.POST.get('doctor_name'),
        test=request.POST.get('test'),
        additional_tests=request.POST.get('additional_tests'),
    )
    doctor_details.save()

    patient_name = request.POST.get('patient_name') 

    flag = request.POST.get('test') 
    if flag == 'mmse': 
        return render(request, 'mmse.html', {'doctor_details': doctor_details,'patient_name': patient_name})
    elif flag == "amst":
        return render(request, 'amst.html', {'doctor_details': doctor_details,'patient_name': patient_name})
    else:
        return HttpResponseBadRequest("Invalid test type provided.")