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
        mobile_num=request.POST['number'],
        city=request.POST['city'],
        state=request.POST['state'],
        country=request.POST['country']
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
        mmse_points = 0

        # Create and save the MMSE answers
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

        # Check day, year, month, date correctness
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
        if mmseans.date == current_date:
            print("date true")
            mmse_points += 1

        # Calculate current season
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

        if objects == recall_obj:
            print("memory recall true")
            mmse_points += 1

        try:
            patient_details = Details.objects.get(patient_name=patient_name)
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

        return render(request, 'test_result.html', {"ans": mmseans, "points": mmse_points})

    
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

        # Initialize variables
        current_hour = datetime.now().hour
        current_year = datetime.now().year
        patient_name = request.POST.get('patient_name')
        match_message = "No patient details found."
        amst_points = 0

        # Retrieve patient details if provided
        patient_details = None
        if patient_name:
            try:
                patient_details = Details.objects.get(patient_name=patient_name)
                if amstans.age == patient_details.patient_age:
                    amst_points += 1
                    match_message = "The age matches with the entered details."
                else:
                    match_message = "The age does not match the entered details."
            except Details.DoesNotExist:
                pass

        # Time match
        match_time = "The time matches with the current time." if amstans.time == current_hour else "The time does not match the current time."
        if amstans.time == current_hour:
            amst_points += 1

        # Year match
        match_year = "The year matches with the current year." if amstans.year == current_year else "The year does not match the current year."
        if amstans.year == current_year:
            amst_points += 1

        # DOB match
        print(amstans.dob)
        print(patient_details.patient_dob)
        if amstans.dob == str(patient_details.patient_dob):
            amst_points += 1
            match_dob = "The date of birth matches with the entered details."
        else:
            match_dob = "The date of birth does not match the entered details."

        # WW1 match
        match_ww1 = "The year of WW1 matches with the entered details." if amstans.ww1 == 1914 else "The year of WW1 does not match the entered details."
        if amstans.ww1 == 1914:
            amst_points += 1

        # Count backwards match
        correct_count = "20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1"
        match_count_backwards = "The count backwards matches with the entered details." if amstans.count_backwards == correct_count else "The count backwards does not match the entered details."
        if amstans.count_backwards == correct_count:
            amst_points += 1

        # Repeat address match
        sanitized_address = "".join(amstans.repeat_address.split())  # Remove spaces
        if sanitized_address == "42weststreet":
            amst_points += 1
            match_address = "The address matches with the entered details."
        else:
            match_address = "The address does not match the entered details."

        # Sunrise match
        match_sunrise = "The sunrise direction matches with the entered details." if amstans.sunrise == "east" else "The sunrise direction does not match the entered details."
        if amstans.sunrise == "east":
            amst_points += 1

        # Prepare the context for rendering
        context = {
            'ans': amstans,
            'match_message': match_message,
            'time_message': match_time,
            'year_message': match_year,
            'dob_message': match_dob,
            'ww1_message': match_ww1,
            'count_message': match_count_backwards,
            'address_message': match_address,
            'sunrise_message': match_sunrise,
            'points': amst_points
        }
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
    