from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('questions_to_answer',views.questions ,name='questions'),
    path('checking_of_dementia',views.checking,name='checking')
]