from django.db import models

# Create your models here.

class Details(models.Model):
    patient_name = models.CharField(max_length=100)
    patient_age = models.IntegerField()
    date = models.DateField()
    mobile_num = models.CharField(max_length=15)

    def __str__(self):
        return self.patient_name

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

class DoctorInfo(models.Model):
    doctor_name = models.CharField(max_length=100)
    test = models.CharField(max_length=255)  # To store MMSE, AMST, etc.
    additional_tests = models.TextField(blank=True, null=True)

    
    def __str__(self):
        return f"Doctor: {self.doctor_name}, Tests: {self.tests}"

class AmstAnswers(models.Model):
    test_name = models.CharField(max_length=255)
    age = models.IntegerField()
    time = models.CharField(max_length=50)
    year = models.IntegerField()
    location = models.CharField(max_length=255)
    recognize_people = models.CharField(max_length=255)
    dob = models.CharField(max_length=20)
    ww1 = models.IntegerField()
    count_backwards = models.CharField(max_length=255)
    repeat_address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.test_name} - {self.age}"