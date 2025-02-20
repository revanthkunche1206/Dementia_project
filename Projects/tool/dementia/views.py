from django.shortcuts import render
from django.http import JsonResponse
import json
import uuid
from django.urls import reverse
from .models import Details
from .models import Answers
from .models import AmstAnswers
from .models import MmseAnswers
from .models import DoctorInfo
from django.http import HttpResponseBadRequest
from datetime import datetime
from django.shortcuts import get_object_or_404

def home(request):
    return render(request,'home.html')

def questions(request):
    
    details = Details(
        patient_name=request.POST['name'],
        patient_dob=request.POST['dob'],
        patient_age=int(request.POST['age']),
        date=request.POST['date'],
        mobile_num=request.POST['number'],
        city=request.POST['city'],
        state=request.POST['state'],
        country=request.POST['country']
    )
    
    details.save()

    print("patient_id=",details.patient_id)
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
        mmse_points = 0
        patient_name = request.POST.get('patient_name', '').strip()
        patient_id = request.POST.get('patient_id', '').strip()

        print("id=",patient_id)


        mmseans = MmseAnswers(
            test_name=request.POST.get('test_name', ''), 
            year=int(request.POST.get('year', '0')),
            season=request.POST.get('season', '').lower(),
            day=request.POST.get('day', '').lower(),
            month=request.POST.get('month', '').capitalize(),
            date=request.POST.get('date', ''),
            state=request.POST.get('state', '').lower(),
            county=request.POST.get('county', '').lower(),
            town=request.POST.get('town', '').lower(),
            hospital=request.POST.get('hospital', ''),
            floor=request.POST.get('floor', ''),
            memory=request.POST.get('memory', '').lower(),
            name_backward=request.POST.get('backward', '').lower(),
            recall=request.POST.get('recall', '').lower(),
            objects_outside=request.POST.get('objects', '').lower(),
            phrase=request.POST.get('phrase', '').lower()
        )
        mmseans.save()

        # Current date-related info
        current_year = datetime.now().year
        month=datetime.now().month
        current_month = datetime.now().strftime("%B")
        current_day = datetime.now().strftime("%A").lower()
        date = datetime.now().day
        current_date=str(current_year)+"-"+str(month)+"-"+str(date)
        patient_name = request.POST.get('patient_name', '')

        

        if mmseans.day == current_day:
            print("day true")
            mmse_points += 1

        if mmseans.year == current_year:
            print("year true")
            mmse_points += 1

        if mmseans.month == current_month:
            print("month true")
            mmse_points += 1

        print(current_date)
        print(mmseans.date)
        ##this on not working
        if mmseans.date == current_date:
            print("date true")
            mmse_points += 1

        month_to_number = {
            "January": 1, "February": 2, "March": 3, "April": 4, "May": 5,
            "June": 6, "July": 7, "August": 8, "September": 9, "October": 10,
            "November": 11, "December": 12
        }
        current_month_num = month_to_number[current_month]
        current_season = ""
        
        if (current_month_num == 3 and int(date) >= 15) or (4 <= current_month_num <= 5 and int(date) <= 15):
            current_season = "spring"
        elif (current_month_num == 5 and int(date) > 15) or (6 <= current_month_num <= 7 and int(date) <= 15):
            current_season = "summer"
        elif (current_month_num == 7 and int(date) > 15) or (8 <= current_month_num <= 9 and int(date) <= 15):
            current_season = "monsoon"
        elif (current_month_num == 9 and int(date) > 15) or (10 <= current_month_num <= 11 and int(date) <= 15):
            current_season = "autumn"
        else:
            current_season = "winter"

        if current_season == mmseans.season:
            print("season true")
            mmse_points += 1

        if patient_name[::-1].lower() == mmseans.name_backward:
            print("name back true")
            mmse_points += 1
        
        objects = sorted(mmseans.memory.split())
        recall_obj = sorted(mmseans.recall.split())

        if objects:
            print("obj true")
            mmse_points+=3

        if objects == recall_obj:
            print("recall true")
            print("memory recall true")
            mmse_points += 3

        hospital_verified = request.POST.get('hospital_verified')
        floor_verified = request.POST.get('floor_verified')
        
        print(f"Hospital verified: {hospital_verified}") 
        print(f"Floor verified: {floor_verified}")
        if hospital_verified == 'yes' and floor_verified == 'yes':
            mmse_points += 2
            print("Added 2 points for both verified")  
        elif hospital_verified == 'yes' or floor_verified == 'yes':
            mmse_points += 1
            print("Added 1 point for one verified")

        if mmseans.phrase=="n pple everydy keeps the doctor wy":
            print("phrase true")
            mmse_points+=3


        objects_verified = request.POST.get('objects_verified')
        print(f"Objects verified: {objects_verified}")  
        if objects_verified == 'yes':
            mmse_points += 1
            print("Added 1 point for objects verified")

        try:
            patient_details = get_object_or_404(Details, patient_name=patient_name, patient_id=patient_id)

            if mmseans.state == patient_details.state.lower():
                print("state true")
                mmse_points += 1
            if mmseans.county == patient_details.country.lower():
                print("country true")
                mmse_points += 1
            if mmseans.town == patient_details.city.lower():
                print("city true")
                mmse_points += 1
        except Details.DoesNotExist:
            print("Patient details not found")
        check_list=[current_date,current_day,current_month,current_year,current_season]
        return render(request, 'test_result_mmse.html', {"check_list":check_list,"patient_details":patient_details,"max_points":20,"patient_name":patient_name,"patient_id":patient_id,"date":current_date,"ans": mmseans, "points": mmse_points})

    
def amst_test(request):
    if request.method == "POST":
        amstans = AmstAnswers(
            test_name=request.POST.get('test_name', ''),
            age=int(request.POST.get('age', 0)),
            time=int(request.POST.get('time', 0)),
            year=int(request.POST.get('year', 0)),
            location=request.POST.get('location', ''),
            recognize_people=request.POST.get('recognizePeople', ''),
            dob=request.POST.get('dob', ''),
            sunrise=request.POST.get('sunrise', '').strip().lower(),
            ww1=int(request.POST.get('ww1', 0)),
            count_backwards=request.POST.get('countBackwards', '').strip(),
            repeat_address=request.POST.get('repeatAddress', '').strip().lower()
        )
        amstans.save()

        current_hour = datetime.now().hour
        current_year = datetime.now().year

        current_year = datetime.now().year
        month=datetime.now().month
        date = datetime.now().day
        current_date=str(current_year)+"-"+str(month)+"-"+str(date)
        patient_name = request.POST.get('patient_name')
        amst_points = 0
        patient_id = request.POST.get('patient_id')
        patient_details = None
        
        if patient_name:
            try:
                patient_details = get_object_or_404(Details, patient_name=patient_name, patient_id=patient_id)
                if amstans.age == patient_details.patient_age:
                    amst_points += 1               
            except Details.DoesNotExist:
                pass

        location_verified = request.POST.get('location_verified')
        if location_verified == 'yes':
            amst_points += 1

        recognition_verified = request.POST.get('recognition_verified')
        if amstans.recognize_people.lower() == 'yes' and recognition_verified == 'yes':
            amst_points += 1

        if amstans.time == current_hour:
            amst_points += 1

        if amstans.year == current_year:
            amst_points += 1

        print(amstans.dob)
        print(patient_details.patient_dob)
        if amstans.dob == str(patient_details.patient_dob):
            amst_points += 1
        
        if amstans.ww1 == 1914:
            amst_points += 1

        correct_count = "20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1"
        if amstans.count_backwards == correct_count:
            amst_points += 1

        sanitized_address = "".join(amstans.repeat_address.split()) 
        if sanitized_address == "42weststreet":
            amst_points += 2
        
        if amstans.sunrise == "east":
            amst_points += 1

        return render(request, 'test_result_amst.html', {"date":current_date,"patient_details": patient_details, "max_points": 11, "points": amst_points})
    
    
def test_taken(request):
    doctor_details = DoctorInfo(
        doctor_name=request.POST.get('doctor_name'),
        test=request.POST.get('test'),
        additional_tests=request.POST.get('additional_tests'),
    )
    doctor_details.save()

    patient_name = request.POST.get('patient_name')
    patient_id = request.POST.get('patient_id')

    flag = request.POST.get('test') 
    if flag == 'mmse': 
        return render(request, 'mmse.html', {'doctor_details': doctor_details,'patient_name': patient_name,'patient_id': patient_id})
    elif flag == "amst":
        return render(request, 'amst.html', {'doctor_details': doctor_details,'patient_name': patient_name,'patient_id': patient_id})
    else:
        return HttpResponseBadRequest("Invalid test type provided.")
    