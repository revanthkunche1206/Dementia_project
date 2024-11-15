from django.db import models

# Create your models here.
class Details:

    patient_name : str
    patient_age : int
    date : str
    mobile_num : int

class Answers:

    ans1 : bool
    ans2 : bool
    ans3 : bool
    ans4 : bool
    ans5 : bool
    ans6 : bool
    ans7 : bool
    ans8 : bool
    ans9 : bool
    ans10 : bool
    ans11 : bool
    ans12 : bool
    ans13 : bool
    ans14 : bool
    ans15 : bool
    ans16 : bool
    ans17 : bool
    ans18 : bool

    test_name: str
    age: int
    time: str
    year: int
    location: str
    recognize_people: str
    dob: str
    ww1: int
    count_backwards: str
    repeat_address: str

class DoctorInfo(models.Model):
    doctor_name = models.CharField(max_length=100)
    test = models.CharField(max_length=255)  # To store MMSE, AMST, etc.
    additional_tests = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Doctor: {self.doctor_name}, Tests: {self.tests}"