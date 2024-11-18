from django.shortcuts import render
from django.urls import reverse
from .models import Details
from .models import Answers
from .models import AmstAnswers
from .models import MmseAnswers
from .models import DoctorInfo
from django.http import HttpResponseBadRequest
from datetime import datetime
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    return render(request,'home.html')

def questions(request):
    
    details = Details(
        patient_name=request.POST['name'],
        patient_dob=request.POST['dob'],
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

def mmse_test(request):
    if request.method == 'POST':
         mmseans= MmseAnswers(
            year=request.POST.get('year', ''),
            season=request.POST.get('season', ''),
            day=request.POST.get('day', ''),
            month=request.POST.get('month', ''),
            date=request.POST.get('date', ''),
            state=request.POST.get('state', ''),
            county=request.POST.get('county', ''),
            town=request.POST.get('town', ''),
            hospital=request.POST.get('hospital', ''),
            floor=request.POST.get('floor', ''),
            memory=request.POST.get('memory', ''),
            backward=request.POST.get('backward', ''),
            recall=request.POST.get('recall', ''),
            objects_outside=request.POST.get('objects', ''),
            phrase=request.POST.get('phrase', '')
        )
         mmseans.save()  
         return render(request, 'test_result.html', {"Mmseans":mmseans})
    
def amst_test(request):
    if request.method == "POST":
        amstans = AmstAnswers(
            test_name=request.POST.get('test_name', ''),
            age=int(request.POST.get('age', 0)),
            time=int(request.POST.get('time', '')),
            year=int(request.POST.get('year', 0)),
            location=request.POST.get('location', ''),
            recognize_people=request.POST.get('recognizePeople', ''),
            dob=request.POST.get('dob', ''),
            sunrise=str(request.POST.get('sunrize','')),
            ww1=int(request.POST.get('ww1', 0)),
            count_backwards=request.POST.get('countBackwards', ''),
            repeat_address=str(request.POST.get('repeatAddress', ''))
        )
        amstans.save()

        current_hour = datetime.now().hour
        current_year = datetime.now().year
        patient_name = request.POST.get('patient_name') 
        match_message = "No patient details found."
        print(str(amstans.count_backwards))
        if patient_name:
            try:
                patient_details = Details.objects.get(patient_name=patient_name)
                if amstans.age == patient_details.patient_age:
                    match_message = "The age matches with the entered details."
                else:
                    match_message = "The age does not match the entered details."
            except Details.DoesNotExist:
                pass

        if amstans.time==current_hour:
            match_time = "The time matches with the current time."
        else:
            match_time = "The time does not match the current time."

        
        if amstans.year==current_year:
            match_year = "The year matches with the current year."
        else:
            match_year = "The year does not match the current year."

        
        if str(amstans.dob)==str(patient_details.patient_dob):
            match_dob = "The date of birth matches with the entered details."
        else:
            match_dob = "The date of birth does not match the entered details."

        if amstans.ww1==1914:
            match_ww1 = "The year of WW1 matches with the entered details."
        else:
            match_ww1 = "The year of WW1 does not match the entered details."

        if amstans.count_backwards=="20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1":
            match_count_backwards = "The count backwards matches with the entered details."
        else:
            match_count_backwards = "The count backwards does not match the entered details."
        
        amstans.repeat_address=(amstans.repeat_address).lower()
        repaddress=""
        for i in amstans.repeat_address:
            if i!=" ":
                repaddress+=i
        if repaddress=="42weststreet":
            match_address = "The address matches with the entered details."
        else:
            match_address = "The address does not match the entered details."
        if amstans.sunrise=="east":
            match_sunrise = "The sunrise direction matches with the entered details."
        else:
            match_sunrise = "The sunrise direction does not match the entered details."
        context = {'responses': amstans, 'match_message': match_message,'time_message':match_time,'year_message':match_year,'dob_message':match_dob,'ww1_message':match_ww1,'count_message':match_count_backwards,'address_message':match_address,'sunrise_message':match_sunrise}
        return render(request, 'test_result.html', context)

        

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