from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('test_taken', views.test_taken, name='test_taken'),
    path('questions_to_answer',views.questions ,name='questions'),
    path('checking_of_dementia',views.checking,name='checking'),
    path('amst_test', views.amst_test, name='amst_test'),
     
]