from django.db import models
import uuid 
# Create your models here.

class Details(models.Model):
    patient_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    patient_name = models.CharField(max_length=100)
    patient_dob = models.DateField()
    patient_age = models.IntegerField()
    date = models.DateField()
    mobile_num = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.patient_name} ({self.patient_id})"

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
    sunrise=models.CharField(max_length=20)
    ww1 = models.IntegerField()
    count_backwards = models.CharField(max_length=255)
    repeat_address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.test_name} - {self.age}"
    
class MmseAnswers(models.Model):
    test_name = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    season = models.CharField(max_length=20)
    day = models.CharField(max_length=20)
    month = models.CharField(max_length=20)
    date = models.DateField()

    state = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    town = models.CharField(max_length=50)
    hospital = models.CharField(max_length=100)
    floor = models.CharField(max_length=50)

    memory = models.CharField(max_length=100)

    name_backward = models.CharField(max_length=100)

    recall = models.CharField(max_length=100)

    objects_outside = models.CharField(max_length=100)

    phrase = models.CharField(max_length=255)

    def __str__(self):
        return f"Assessment on {self.date} - {self.hospital}"